import numpy as np
import matplotlib.pyplot as plt

# Class representing a single link of the robot arm
class Link:
    def __init__(self, length: float):
        self.length = length  # Length of the link, representing the physical segment of the robot arm


# Class representing a joint, with an associated angle in radians
class Joint:
    def __init__(self, angle_deg: float):
        # Initialize the joint with the given angle (converted from degrees to radians)
        self.angle = np.radians(angle_deg)

    def set_angle(self, angle_deg: float):
        # Update the joint's angle (again, convert to radians)
        self.angle = np.radians(angle_deg)


# Main RobotArm class containing the structure and kinematics
class RobotArm:
    def __init__(self):
        self.links = []   # List to hold all the link segments of the robot arm
        self.joints = []  # List to hold corresponding joints between each link

    # Add a link-joint pair to the robot arm
    def add_segment(self, length: float, angle_deg: float):
        self.links.append(Link(length))           # Create and store a new Link
        self.joints.append(Joint(angle_deg))      # Create and store a new Joint

    # Set the angle of a specific joint by index
    def set_joint_angle(self, index: int, angle_deg: float):
        if 0 <= index < len(self.joints):
            self.joints[index].set_angle(angle_deg)
        else:
            print("Invalid joint index")

    # Perform forward kinematics to calculate joint positions
    def forward_kinematics(self):
        x_positions = [0]  # Starting X position from origin
        y_positions = [0]  # Starting Y position from origin
        current_angle = 0  # Cumulative angle as we progress through each joint

        # Loop through each segment and calculate its endpoint based on current angle
        for i in range(len(self.links)):
            current_angle += self.joints[i].angle  # Accumulate angles
            x = x_positions[-1] + self.links[i].length * np.cos(current_angle)  # New X position
            y = y_positions[-1] + self.links[i].length * np.sin(current_angle)  # New Y position
            x_positions.append(x)
            y_positions.append(y)

        return x_positions, y_positions

    # Inverse kinematics calculation, implemented for 2-link arms only
    def inverse_kinematics_2link(self, x_target, y_target):
        if len(self.links) != 2:
            raise ValueError("Inverse kinematics is implemented only for 2-link arms.")

        l1 = self.links[0].length
        l2 = self.links[1].length

        # Use Law of Cosines to calculate angle at the second joint
        D = (x_target ** 2 + y_target ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)

        if abs(D) > 1:
            print("Target is unreachable due to physical limits of the arm.")
            return

        # Solve for joint angles
        theta2 = np.arccos(D)  # Elbow angle
        theta1 = np.arctan2(y_target, x_target) - np.arctan2(l2 * np.sin(theta2), l1 + l2 * np.cos(theta2))  # Shoulder angle

        # Update joint angles in the robot arm
        self.joints[0].angle = theta1
        self.joints[1].angle = theta2

    # Plot the current configuration of the robot arm
    def plot(self):
        x, y = self.forward_kinematics()  # Get positions of all joints/links

        plt.ion()  # Turn on interactive mode to allow multiple plots
        plt.figure(figsize=(8, 8))  # Define figure size for consistent plotting
        plt.plot(x, y, '-o', linewidth=4, markersize=8, color='royalblue')  # Draw the arm
        plt.title("Robot Arm Kinematics")
        plt.xlabel("X Position")
        plt.ylabel("Y Position")
        plt.grid(True)
        plt.axis('equal')  # Ensure uniform scaling
        plt.xlim(-20, 100)  # Set limits for X axis
        plt.ylim(-20, 100)  # Set limits for Y axis
        plt.draw()  # Display the plot
        plt.pause(0.001)  # Short pause to allow updates in interactive mode


# Function to interact with the user and simulate robot arm behavior

def run_simulation():
    arm = RobotArm()  # Create a RobotArm object

    # Ask the user how many segments (links) the arm should have
    num_links = int(input("Enter number of links (2 recommended): "))
    for i in range(num_links):
        length = float(input(f"Enter length of link {i + 1}: "))  # Input link length
        angle = float(input(f"Enter initial angle (in degrees) for joint {i + 1}: "))  # Input initial angle
        arm.add_segment(length, angle)  # Add the segment to the robot arm

    # Main loop for user interaction
    while True:
        print("\nOptions:")
        print("1. Set joint angles")
        print("2. Move to position using inverse kinematics")
        print("3. Plot current arm configuration")
        print("4. Exit")
        choice = input("Choose an option: ")  # Menu selection

        if choice == '1':
            # Set new angles for each joint
            for i in range(len(arm.joints)):
                angle = float(input(f"Enter new angle (in degrees) for joint {i + 1}: "))
                arm.set_joint_angle(i, angle)
        elif choice == '2':
            # Move end-effector to new position using IK
            x = float(input("Enter target x position: "))
            y = float(input("Enter target y position: "))
            arm.inverse_kinematics_2link(x, y)
        elif choice == '3':
            # Plot the arm's current configuration
            arm.plot()
        elif choice == '4':
            # Exit simulation
            print("Exiting.")
            break
        else:
            print("Invalid option. Try again.")


# Only run the simulation if this file is executed directly
if __name__ == "__main__":
    run_simulation()
