import numpy as np
import matplotlib.pyplot as plt


class Link:
    def __init__(self, length: float):
        self.length = length


class Joint:
    def __init__(self, angle_deg: float):
        self.angle = np.radians(angle_deg)

    def set_angle(self, angle_deg: float):
        self.angle = np.radians(angle_deg)


class RobotArm:
    def __init__(self):
        self.links = []
        self.joints = []

    def add_segment(self, length: float, angle_deg: float):
        self.links.append(Link(length))
        self.joints.append(Joint(angle_deg))

    def set_joint_angle(self, index: int, angle_deg: float):
        if 0 <= index < len(self.joints):
            self.joints[index].set_angle(angle_deg)
        else:
            print("Invalid joint index")

    def forward_kinematics(self):
        x_positions = [0]
        y_positions = [0]
        current_angle = 0

        for i in range(len(self.links)):
            current_angle += self.joints[i].angle
            x = x_positions[-1] + self.links[i].length * np.cos(current_angle)
            y = y_positions[-1] + self.links[i].length * np.sin(current_angle)
            x_positions.append(x)
            y_positions.append(y)

        return x_positions, y_positions

    def inverse_kinematics_2link(self, x_target, y_target):
        if len(self.links) != 2:
            raise ValueError("Inverse kinematics is implemented only for 2-link arms.")

        l1 = self.links[0].length
        l2 = self.links[1].length
        D = (x_target ** 2 + y_target ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)

        if abs(D) > 1:
            print("Target is unreachable.")
            return

        theta2 = np.arccos(D)
        theta1 = np.arctan2(y_target, x_target) - np.arctan2(l2 * np.sin(theta2), l1 + l2 * np.cos(theta2))

        self.joints[0].angle = theta1
        self.joints[1].angle = theta2

    def plot(self):
        x, y = self.forward_kinematics()

        plt.ion()  # Turn on interactive mode
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, '-o', linewidth=4, markersize=8, color='royalblue')
        plt.title("Robot Arm Kinematics")
        plt.xlabel("X Position")
        plt.ylabel("Y Position")
        plt.grid(True)
        plt.axis('equal')
        plt.xlim(0, 100)
        plt.ylim(0, 100)
        plt.draw()
        plt.pause(0.001)


def run_simulation():
    arm = RobotArm()
    num_links = int(input("Enter number of links (2 recommended): "))
    for i in range(num_links):
        length = float(input(f"Enter length of link {i + 1}: "))
        angle = float(input(f"Enter initial angle (in degrees) for joint {i + 1}: "))
        arm.add_segment(length, angle)

    while True:
        print("\nOptions:")
        print("1. Set joint angles")
        print("2. Move to position using inverse kinematics")
        print("3. Plot current arm configuration")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            for i in range(len(arm.joints)):
                angle = float(input(f"Enter new angle (in degrees) for joint {i + 1}: "))
                arm.set_joint_angle(i, angle)
        elif choice == '2':
            x = float(input("Enter target x position: "))
            y = float(input("Enter target y position: "))
            arm.inverse_kinematics_2link(x, y)
        elif choice == '3':
            arm.plot()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    run_simulation()
