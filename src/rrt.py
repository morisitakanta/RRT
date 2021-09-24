import numpy as np
import plotting
import env
import utils

class Node:
    def __init__(self, n):
        self.x = n[0]
        self.y = n[1]
        self.parent = None
        self.cost = 0

class GridMap:
    def __init__(self,size):
        self.env = env.Env()
        self.x_range = self.env.x_range
        self.y_range = self.env.y_range
        self.g_size = size

        self.utils = utils.Utils()

    def is_occupied(self, grid):
        return self.utils.is_inside_obs(grid)

    def create_grid_map(self):
        g_map = []
        for i in range(self.x_range[0], self.x_range[1]+self.g_size, self.g_size):
            y_ray=[]
            for j in range(self.y_range[0], self.y_range[1]+self.g_size, self.g_size):
                node = Node((i,j))
                y_ray.append(int(self.is_occupied(node)))
                # print(self.is_occupied(node))
            g_map.append(y_ray)
        # self.show(g_map)
        return g_map

    def show(self, g_map):
        for i in range(len(g_map)-1, -1, -1):
            print(g_map[i])

class Rrt:
    def __init__(self, s_start, s_goal, grid_map, iter_max, goal_sample_rate, grid_size):
        self.s_start = Node(s_start)
        self.s_goal = Node(s_goal)
        self.iter_max = iter_max
        self.goal_sample_rate = goal_sample_rate
        self.grid_map = grid_map
        self.grid_size = grid_size

        self.env = env.Env()
        self.plotting = plotting.Plotting(s_start,s_goal)

        self.x_range = self.env.x_range
        self.y_range = self.env.y_range
        self.vertex = [self.s_start]

    def planning(self):
        node_now = []
        node_now.append(self.s_start)
        for i in range(self.iter_max):
            node_next = None
            for n_now in node_now:
                node_next = self.generate_node_next(n_now)

                if node_next != None:
                    for node in node_next:
                        self.vertex.append(node)
                        if self.goal_detecter(node, self.s_goal) and len(self.vertex) > 2:
                            return self.generate_path(node, self.s_goal)
                    
            if len(node_next) > 0:
                node_selected = self.select_node_now(node_next)
            else :
                node_selected = self.select_node_now(self.vertex)
            node_now.clear
            for n_now in node_selected:
                node_now.append(n_now)
        vertex_len = len(self.vertex)
        return self.generate_path(self.vertex[vertex_len-1], self.vertex[vertex_len-1])

# functions
    def generate_random_node(self, goal_sample_rate, grid_size, center, size_x, size_y):
        if np.random.rand() > goal_sample_rate:
            return Node((np.random.randint(center.x - int(size_x/2), center.x + int(size_x/2)),
                         np.random.randint(center.y - int(size_y/2), center.y + int(size_y/2))))
        return Node((0,0))

    def generate_node_next(self, node_now):
        node_next = []
        node_next.append(node_now)
        expand_size = 7
        rand_node_num = 10
        for i in range(rand_node_num):
            node = self.generate_random_node(self.goal_sample_rate, self.grid_size, node_now, expand_size, expand_size )
            node.parent = node_now
            if node.x > self.x_range[0] and node.x < self.x_range[1] and node.y > self.y_range[0] and node.y < self.y_range[1]:
                if self.grid_map[node.x][node.y] != 1:
                    flag_nn = True
                    flag_vt = True
                    for nn in node_next:
                        if node.x == nn.x and node.y == nn.y:
                            flag_nn = False
                            break
                    for vt in self.vertex:
                        if node.x == vt.x and node.y == vt.y:
                            flag_vt = False
                            break
                    if flag_nn and flag_vt:
                        node_next.append(node)

        if len(node_next) < 1:
            return None
        del node_next[0]
        return node_next

    def select_node_now(self, node_list):
        select_num = 3
        if len(node_list) > select_num:
            return np.random.choice(node_list, size=select_num, replace=False)
        return node_list

    def goal_detecter(self, node, goal):
        if node.x == goal.x and node.y == goal.y:
            return True
        return False

    def generate_path(self, node_nearest, goal):
        path = [(goal.x, goal.y)]
        node_now = node_nearest
        while node_now.parent != None:
            path.append((node_now.x, node_now.y))
            node_now = node_now.parent
        path.append((self.s_start.x, self.s_start.y))
        return path
# 

def main():
    x_start = (48, 3)
    x_goal = (5, 25)
    grid_size = 1

    grid = GridMap(grid_size)
    grid_map = grid.create_grid_map()

    rrt = Rrt(x_start, x_goal, grid_map, 10000, 0.5, grid_size)
    path = rrt.planning()
    rrt.plotting.animation(rrt.vertex, path, "RRT", True)
    print("test")


if __name__ =='__main__':
    main()