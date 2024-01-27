#     "all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
#     "x": float,                            # agent's x-coordinate in meters
#     "y": float,                            # agent's y-coordinate in meters
#     "closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
#     "closest_waypoints": [int, int],       # indices of the two nearest waypoints.
#     "distance_from_center": float,         # distance in meters from the track center 
#     "is_crashed": Boolean,                 # Boolean flag to indicate whether the agent has crashed.
#     "is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not. 
#     "is_offtrack": Boolean,                # Boolean flag to indicate whether the agent has gone off track.
#     "is_reversed": Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
#     "heading": float,                      # agent's yaw in degrees
#     "objects_distance": [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
#     "objects_heading": [float, ],          # list of the objects' headings in degrees between -180 and 180.
#     "objects_left_of_center": [Boolean, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
#     "objects_location": [(float, float),], # list of object locations [(x,y), ...].
#     "objects_speed": [float, ],            # list of the objects' speeds in meters per second.
#     "progress": float,                     # percentage of track completed
#     "speed": float,                        # agent's speed in meters per second (m/s)
#     "steering_angle": float,               # agent's steering angle in degrees
#     "steps": int,                          # number steps completed
#     "track_length": float,                 # track length in meters.
#     "track_width": float,                  # width of the track
#     "waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center

def get_param():
    param = {}

    param["all_wheels_on_track"] = True
    param["x"] = 1.0
    param["y"] = 1.0
    param["closest_objects"]        = [1,2]
    param["closest_waypoints"]      = [1,2]
    param["distance_from_center"]   = 2.0
    param["is_crashed"]             = False
    param["is_left_of_center"]      = True
    param["is_offtrack"]            = False
    param["is_reversed"]            = False
    param["heading"]                = 2.0
    # object related
    param["objects_distance"]       = [1.0,2.0]
    param["objects_heading"]        = [1.0,2.0]
    param["objects_left_of_center"] = [True,True]
    param["objects_location"]       = [ (1.0,1.0), (2.0,2.0)]
    param["objects_speed"]          = [1.0, 2.0]

    param["progress"]           = 0.5
    param["speed"]              = 0.5
    param["steering_angle"]     = 0.5
    param["steps"]              = 5
    param["track_length"]       = 10 
    param["track_width"]        = 3 
    param["waypoints"]          = [(0.1, 0.1),(0.2, 0.2), (0.3, 0.3), (0.4, 0.4),  (0.5, 0.5)]
    # print("get_param(): \n" + str(param))
    return param