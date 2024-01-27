import math
import numpy as np
# import scipy.spatial as spt


optimal_data = [[5.6042, -0.28762, 4.0, 0.06995], [5.61376, 0.02211, 3.94854, 0.07848],
                [5.6076, 0.29136, 3.87155, 0.06957], [5.59232, 0.51899, 3.79889, 0.06006],
                [5.57006, 0.72579, 3.72972, 0.05576], [5.54164, 0.91923, 3.67617, 0.05319],
                [5.5074, 1.10324, 3.6321, 0.05153], [5.46744, 1.28027, 3.60425, 0.05035],
                [5.42163, 1.45206, 3.57759, 0.0497], [5.36967, 1.61999, 3.55784, 0.04941],
                [5.31107, 1.78528, 3.5448, 0.04947], [5.24514, 1.9491, 3.53942, 0.04989],
                [5.17086, 2.11275, 3.53871, 0.05079], [5.08679, 2.27772, 3.52857, 0.05247],
                [4.99068, 2.44597, 3.52462, 0.05498], [4.87893, 2.62034, 3.52462, 0.05876],
                [4.7455, 2.80501, 3.52462, 0.06464], [4.58089, 3.00516, 3.52462, 0.07352],
                [4.37752, 3.21932, 3.52462, 0.08379], [4.16239, 3.41399, 3.52462, 0.08232],
                [3.97678, 3.56022, 3.53192, 0.0669], [3.81137, 3.67601, 3.54262, 0.057],
                [3.6569, 3.77316, 3.5763, 0.05103], [3.50759, 3.85802, 3.61739, 0.04748],
                [3.3597, 3.93412, 3.68345, 0.04515], [3.21049, 4.00364, 3.77166, 0.04364],
                [3.05767, 4.06799, 3.88167, 0.04272], [2.89909, 4.12818, 4.0, 0.04241], [2.73249, 4.18496, 4.0, 0.044],
                [2.55534, 4.23893, 4.0, 0.0463], [2.36447, 4.29061, 4.0, 0.04944], [2.15561, 4.34051, 4.0, 0.05368],
                [1.9229, 4.38916, 4.0, 0.05944], [1.65736, 4.43724, 4.0, 0.06746], [1.34457, 4.48572, 4.0, 0.07913],
                [0.95928, 4.5362, 4.0, 0.09715], [0.45164, 4.59176, 4.0, 0.12767], [-0.274, 4.65847, 3.48162, 0.2093],
                [-1.14986, 4.7327, 2.71417, 0.32385], [-2.02898, 4.80679, 2.29693, 0.3841],
                [-2.90946, 4.88083, 2.03998, 0.43313], [-3.78995, 4.95487, 1.86071, 0.47487],
                [-4.2029, 4.96536, 1.73112, 0.23862], [-4.46085, 4.94887, 1.641, 0.15751],
                [-4.64909, 4.91809, 1.57682, 0.12097], [-4.79653, 4.87777, 1.53181, 0.09978],
                [-4.9165, 4.83041, 1.50805, 0.08553], [-5.01606, 4.77751, 1.5, 0.07516],
                [-5.09937, 4.72009, 1.5, 0.06745], [-5.16918, 4.65893, 1.5, 0.06187], [-5.22732, 4.59461, 1.5, 0.0578],
                [-5.27506, 4.52761, 1.5, 0.05485], [-5.31335, 4.45831, 1.5, 0.05278],
                [-5.34288, 4.38703, 1.50924, 0.05113], [-5.36423, 4.31401, 1.53429, 0.04958],
                [-5.37785, 4.23944, 1.57853, 0.04803], [-5.38412, 4.16335, 1.64121, 0.04652],
                [-5.38335, 4.08564, 1.73119, 0.04489], [-5.37578, 4.00593, 1.84963, 0.04329],
                [-5.36148, 3.92344, 2.008, 0.04169], [-5.34021, 3.83682, 2.24017, 0.03982],
                [-5.3114, 3.74389, 2.57653, 0.03776], [-5.27394, 3.64148, 3.12957, 0.03485],
                [-5.22651, 3.5258, 4.0, 0.03126], [-5.17016, 3.39682, 4.0, 0.03519], [-5.052, 3.12374, 4.0, 0.07439],
                [-4.93249, 2.84269, 4.0, 0.07635], [-4.81123, 2.55134, 4.0, 0.07889], [-4.68774, 2.24696, 4.0, 0.08212],
                [-4.5616, 1.92699, 4.0, 0.08599], [-4.43228, 1.58846, 4.0, 0.0906], [-4.29917, 1.22791, 4.0, 0.09609],
                [-4.16153, 0.84111, 4.0, 0.10264], [-4.01841, 0.42272, 4.0, 0.11055], [-3.8684, -0.03511, 4.0, 0.12045],
                [-3.70941, -0.54381, 3.67827, 0.1449], [-3.53776, -1.12331, 3.28804, 0.18381],
                [-3.34522, -1.81625, 3.03042, 0.23732], [-3.13243, -2.4932, 2.84898, 0.24907],
                [-2.96355, -2.92802, 2.7125, 0.17197], [-2.81501, -3.24219, 2.63041, 0.13211],
                [-2.67648, -3.48616, 2.59707, 0.10803], [-2.54273, -3.68429, 2.58299, 0.09255],
                [-2.41068, -3.84998, 2.58299, 0.08203], [-2.27834, -3.99111, 2.58299, 0.0749],
                [-2.14417, -4.11253, 2.58299, 0.07006], [-2.00691, -4.21758, 2.58299, 0.06692],
                [-1.8654, -4.30865, 2.58299, 0.06515], [-1.71846, -4.38721, 2.61217, 0.06379],
                [-1.56485, -4.45435, 2.66745, 0.06285], [-1.40312, -4.51072, 2.75637, 0.06214],
                [-1.23151, -4.55664, 2.88207, 0.06164], [-1.04776, -4.59212, 3.04338, 0.06149],
                [-0.8487, -4.6168, 3.25864, 0.06155], [-0.62965, -4.62989, 3.5377, 0.06203],
                [-0.38282, -4.62981, 3.91809, 0.063], [-0.09312, -4.61338, 4.0, 0.07254],
                [0.27762, -4.57233, 4.0, 0.09325], [0.94518, -4.45789, 4.0, 0.16932],
                [1.78835, -4.26767, 3.90099, 0.22157], [2.43842, -4.07233, 3.72339, 0.1823],
                [2.91307, -3.89344, 3.60373, 0.14075], [3.28468, -3.72528, 3.50107, 0.1165],
                [3.59017, -3.56324, 3.43136, 0.10078], [3.84973, -3.40432, 3.39161, 0.08974],
                [4.0752, -3.24649, 3.3753, 0.08154], [4.27397, -3.08831, 3.3753, 0.07526],
                [4.45122, -2.92865, 3.3753, 0.07068], [4.61041, -2.76656, 3.3753, 0.06731],
                [4.75408, -2.60121, 3.3753, 0.0649], [4.88415, -2.43181, 3.3753, 0.06327],
                [5.00203, -2.25761, 3.37888, 0.06225], [5.10877, -2.0778, 3.40306, 0.06144],
                [5.20514, -1.89156, 3.44961, 0.06079], [5.29172, -1.69794, 3.49736, 0.06064],
                [5.36875, -1.49579, 3.56815, 0.06063], [5.43634, -1.28373, 3.64596, 0.06105],
                [5.49434, -1.05994, 3.73698, 0.06186], [5.54232, -0.82198, 3.83629, 0.06328],
                [5.57944, -0.56632, 3.94931, 0.06542]]


class Reward:
    def __init__(self):
        global optimal_data
        self.old_point = 0
        self.new_point = 0
        self.old_dis = 0
        self.new_dis = 0
        self.optimal_waypoints, self.optimal_velocity = self.extract_optimal_data(optimal_data)

    def extract_optimal_data(self):
        optimal_waypoints, optimal_velocity = [], []
        for i in range(len(optimal_data) + 1):
            optimal_waypoints.append([optimal_data[i][0],optimal_data[i][1]])
            optimal_velocity.append(optimal_data[i][2])
        return optimal_waypoints, optimal_velocity

    def search_two_nearest_points(self,target):
        target = np.array(target)
        points_with_dis = []
        for i in range(len(self.optimal_waypoints)):
            points_with_dis.append([self.optimal_waypoints[i],i,np.linalg.norm(target-i)]) # Format: [[x,y],index,distance]
        points_with_dis = sorted(points_with_dis,key=lambda points_with_dis:points_with_dis[2])
        return [points_with_dis[0][0],points_with_dis[1][0]], [points_with_dis[0][1],points_with_dis[1][1]]

    def calculate_rewards(self, params):

        current_xy, current_closest_waypoint, speed = [params['x'], params['y']], params['closest_waypoints'], params['speed']

        next_third_point = params['waypoints'][int(current_closest_waypoint[1] + 2)]
        # self.new_dis, closest_waypoints_index = spt.KDTree(optimal_waypoints).query(current_xy, k=2)
        self.new_dis, closest_waypoints_index = search_two_nearest_points(self, target)
        self.new_point = closest_waypoints_index[1]
        p1 = np.array(optimal_waypoints[closest_waypoints_index[0]])
        p2 = np.array(optimal_waypoints[closest_waypoints_index[1]])
        dis_to_centre = np.abs(np.cross(p2 - p1, p1 - np.array(current_xy)) / np.linalg.norm(p2 - p1))
        rewards = 0

        if not params['is_offtrack']:

            # Reward the agent if drive towards the optimal point
            if self.old_point != self.new_point:
                self.old_point = self.new_point
            else:
                if self.new_dis < self.old_dis:
                    rewards += self.new_dis - self.old_dis
                    self.old_dis = self.new_dis

            # Reward the agent for sticking to the optimal path
            if dis_to_centre == 0:
                rewards += 1
            else:
                rewards += (1 - dis_to_centre) ** 0.5

            # Reward the agent for following the optimal speed
            rewards += (1 - abs(speed - optimal_velocity[closest_waypoints_index[1]])) ** 0.4

            # Give the agent additional rewards for following exact point in the optimal path
            if current_xy in optimal_waypoints:
                rewards += 1

            k_current = (current_xy[1] - current_closest_waypoint[1]) / (current_xy[0] - current_closest_waypoint[0])
            k_target = (current_closest_waypoint[1] - next_third_point[1]) / (
                    current_closest_waypoint[0] - next_third_point[0])
            rewards += math.cos(math.atan((k_current - k_target) / (1 + k_current * k_target)))

        return float(rewards)


reward_obj = Reward()


def reward_function(params):
    rewards = reward_obj.calculate_rewards(params)
    return rewards
