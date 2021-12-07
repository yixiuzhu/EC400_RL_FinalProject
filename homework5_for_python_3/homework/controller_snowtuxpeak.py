import pystk


def control(aim_point, current_vel, steer_gain=6, skid_thresh=0.35, target_vel=25):
    import numpy as np
    #this seems to initialize an object
    action = pystk.Action()

    if aim_point[0] < -0.60 or aim_point[0] > 0.60:
        target_vel = 14

    #compute acceleration
    action.acceleration = np.clip(target_vel - current_vel ,0,1)

    if current_vel > target_vel:
    	action.brake = True
    	action.nitro = False
    else:
    	action.brake = False
    	action.nitro = True


    # Compute steering
    if aim_point[0] > 0.8:
        action.steer = 8 * np.clip(8 * aim_point[0], -1, 1)
    else:
        action.steer = np.clip(steer_gain * aim_point[0], -1, 1)

    # Compute skidding
    if abs(aim_point[0]) > skid_thresh:
        action.drift = True
    else:
        action.drift = False




    return action


if __name__ == '__main__':
    from utils import PyTux
    from argparse import ArgumentParser

    def test_controller(args):
        import numpy as np
        pytux = PyTux()
        for t in args.track:
            #it seems that steps measures the number of steps until termination (with max_frames=1000 ensuring termination after 1000 steps)
            #how far measures the amount traversed by the cart
            steps, how_far = pytux.rollout(t, control, max_frames=1000, verbose=args.verbose)
            print(steps, how_far)
        pytux.close()


    parser = ArgumentParser()
    parser.add_argument('track', nargs='+')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    test_controller(args)
