import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Size of the grid (50x50)
grid_size = 50

# Start with a random grid of 0s and 1s (dead and alive cells)
grid = np.random.choice([0, 1], size=(grid_size, grid_size))

def update(frameNum, img, grid):
    # Copy the grid to make changes without messing up the current state
    new_grid = grid.copy()
    
    # Go through every cell in the grid
    for i in range(grid_size):
        for j in range(grid_size):
            # Add up all the neighbors (8 of them, wrapping around the edges)
            total = (grid[i, (j-1)%grid_size] + grid[i, (j+1)%grid_size] +
                     grid[(i-1)%grid_size, j] + grid[(i+1)%grid_size, j] +
                     grid[(i-1)%grid_size, (j-1)%grid_size] + grid[(i-1)%grid_size, (j+1)%grid_size] +
                     grid[(i+1)%grid_size, (j-1)%grid_size] + grid[(i+1)%grid_size, (j+1)%grid_size])
            
            # Apply the Game of Life rules
            if grid[i, j] == 1:
                # Cell dies unless it has 2 or 3 neighbors
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                # Dead cell comes to life if it has exactly 3 neighbors
                if total == 3:
                    new_grid[i, j] = 1
    
    # Update the image to reflect the new grid
    img.set_data(new_grid)
    
    # Pass the updated grid to the next iteration
    grid[:] = new_grid[:]
    return img,

# Set up the plot for animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='gray')

# Run the animation: update the grid every 100 milliseconds
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), frames=10, interval=100, save_count=50)

plt.show()
