import grid
import rrt

def main():
    x_start = (48, 3)
    x_goal = (5, 25)
    grid_size = 1

    g_map = grid.GridMap(grid_size)
    grid_map = g_map.create_grid_map()

    r = rrt.Rrt(x_start, x_goal, grid_map, 10000, 0.5, grid_size)
    path = r.planning()
    r.plotting.animation(r.vertex, path, "RRT", True)
    print("test")


if __name__ =='__main__':
    main()