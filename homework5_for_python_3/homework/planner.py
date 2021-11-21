import torch
import torch.nn.functional as F


def spatial_argmax(logit):
    """
    Compute the soft-argmax of a heatmap
    :param logit: A tensor of size BS x H x W
    :return: A tensor of size BS x 2 the soft-argmax in normalized coordinates (-1 .. 1)
    """
    weights = F.softmax(logit.view(logit.size(0), -1), dim=-1).view_as(logit)
    return torch.stack(((weights.sum(1) * torch.linspace(-1, 1, logit.size(2)).to(logit.device)[None]).sum(1),
                        (weights.sum(2) * torch.linspace(-1, 1, logit.size(1)).to(logit.device)[None]).sum(1)), 1)


class Planner(torch.nn.Module):
    def __init__(self):

        super().__init__()

        layers = []
        # block 1
        layers.append(torch.nn.Conv2d(in_channels=3, out_channels=64, padding=1, kernel_size=3, stride=1))
        layers.append(torch.nn.BatchNorm2d(64))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.Conv2d(in_channels=64, out_channels=64, padding=1, kernel_size=3, stride=1))
        layers.append(torch.nn.BatchNorm2d(64))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.MaxPool2d(kernel_size=2, stride=2))

        # block 2
        layers.append(torch.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1))
        layers.append(torch.nn.BatchNorm2d(128))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1, padding=1))
        layers.append(torch.nn.BatchNorm2d(128))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.MaxPool2d(kernel_size=2, stride=2))

        # block 3
        layers.append(torch.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1, stride=1))
        layers.append(torch.nn.BatchNorm2d(256))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1, stride=1))
        layers.append(torch.nn.BatchNorm2d(256))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1, stride=1))
        layers.append(torch.nn.BatchNorm2d(256))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.MaxPool2d(kernel_size=2, stride=2))

        # block 4
        layers.append(torch.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, padding=1, stride=1))
        layers.append(torch.nn.BatchNorm2d(512))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1, stride=1))
        layers.append(torch.nn.BatchNorm2d(512))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1, stride=1))
        layers.append(torch.nn.BatchNorm2d(512))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.MaxPool2d(kernel_size=2, stride=2))

        # block 5
        layers.append(torch.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1, stride=1))
        layers.append(torch.nn.BatchNorm2d(512))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1, stride=1))
        layers.append(torch.nn.BatchNorm2d(512))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1, stride=1))
        layers.append(torch.nn.BatchNorm2d(512))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.MaxPool2d(kernel_size=2, stride=2))

        layers.append(torch.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=3, padding=1))
        layers.append(torch.nn.BatchNorm2d(256))
        layers.append(torch.nn.ReLU(inplace=True))
        layers.append(torch.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=3, padding=1))
        layers.append(torch.nn.BatchNorm2d(128))
        layers.append(torch.nn.ReLU(inplace=True))
        layers.append(torch.nn.Conv2d(128,1,1))

        #layers.append(torch.nn.Conv2d(3,16,5,2,2))
        #layers.append(torch.nn.ReLU())
        #layers.append(torch.nn.Conv2d(512,1,5,2,2))
        
        self._conv = torch.nn.Sequential(*layers)

        #classifier = []
        #classifier.append(torch.nn.Linear(in_features=6144, out_features=4096))
        #classifier.append(torch.nn.ReLU())
        #classifier.append(torch.nn.Dropout(p=0.5))
        #classifier.append(torch.nn.Linear(in_features=4096, out_features=4096))
        #classifier.append(torch.nn.ReLU())
        #classifier.append(torch.nn.Dropout(p=0.5))
        #classifier.append(torch.nn.Linear(in_features=4096, out_features=1))

        #self.classifier = torch.nn.Sequential(*classifier)

    def forward(self, img):
        """
        Your code here
        Predict the aim point in image coordinate, given the supertuxkart image
        @img: (B,3,96,128)
        return (B,2)
        """
        x = self._conv(img)
        #x = x.view(x.size(0), -1)
        #x = self.classifier(x)
        
        return spatial_argmax(x[:, 0])
        # return self.classifier(x.mean(dim=[-2, -1]))


def save_model(model):
    from torch import save
    from os import path
    if isinstance(model, Planner):
        return save(model.state_dict(), path.join(path.dirname(path.abspath(__file__)), 'planner.th'))
    raise ValueError("model type '%s' not supported!" % str(type(model)))


def load_model():
    from torch import load
    from os import path
    r = Planner()
    r.load_state_dict(load(path.join(path.dirname(path.abspath(__file__)), 'planner.th'), map_location='cpu'))
    return r


if __name__ == '__main__':
    from controller import control
    from utils import PyTux
    from argparse import ArgumentParser


    def test_planner(args):
        # Load model
        planner = load_model().eval()
        pytux = PyTux()
        for t in args.track:
            steps, how_far = pytux.rollout(t, control, planner=planner, max_frames=1000, verbose=args.verbose)
            print(steps, how_far)
        pytux.close()


    parser = ArgumentParser("Test the planner")
    parser.add_argument('track', nargs='+')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    test_planner(args)
