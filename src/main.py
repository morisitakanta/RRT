from matplotlib.colors import get_named_colors_mapping
import grid
import rrt

def main():
    # x_start = (4, 4)
    # x_goal = (46, 28)
    x_start = (46, 28)
    x_goal = (30, 4)
    grid_size = 1

    g_map = grid.GridMap(1) 
    grid_map = g_map.create_reduced_grid_map()
    # g_map.show(grid_map)
    r = rrt.Rrt(x_start, x_goal, grid_map, 10000, 0.0, grid_size)
    path = r.planning(realtime_animation = False)
    print(len(path))
    r.plotting.animation(r.vertex, path, "RRT", False)
    
if __name__ =='__main__':
    main()