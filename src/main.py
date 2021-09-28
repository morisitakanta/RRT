import grid
import rrt

def main():
    # x_start = (5, 3)
    x_start = (25, 15)
    x_goal = (47, 25)
    grid_size = 3

    g_map = grid.GridMap(1)
    grid_map = g_map.create_grid_map()

    r = rrt.Rrt(x_start, x_goal, grid_map, 10000, 0.0, grid_size)
    path = r.planning(realtime_animation = False)
    print(len(path))
    r.plotting.animation(r.vertex, path, "RRT", True)
    
if __name__ =='__main__':
    main()