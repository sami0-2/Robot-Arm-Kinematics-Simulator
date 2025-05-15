# 🤖 Robot Arm Kinematics Simulator

This is a simple Python-based simulator for modeling and visualizing the forward and inverse kinematics of a 2D robot arm. It allows users to interactively define arm segments, set joint angles, and move the arm to a specific position using inverse kinematics (for 2-link arms only).

---

## 📦 Features

- Object-oriented design using classes for `Link`, `Joint`, and `RobotArm`.
- Interactive terminal-based interface for user input and control.
- Forward kinematics to calculate and visualize current arm pose.
- Inverse kinematics solver (for 2-link arms) to reach a desired target.
- Real-time plotting with Matplotlib in interactive mode.
- Ability to plot multiple arm configurations without closing previous plots.
---

## 🚀 How to Run

### ✅ Requirements

Make sure you have Python 3.6+ installed.

Install the required Python libraries using:

```bash
pip install numpy matplotlib
```

## ▶️ Running the Program

Run the program with:
```bash
python robot_arm_simulator.py
```
Follow the on-screen prompts to:
1. Enter the number of links (2 is required for inverse kinematics).
2. Enter the length and initial angle for each joint.
3. Choose an option to:
  Updates joint angles manually,
  Use inverse kinematics to move the arm to a specific (x, y) position,
  Plot the arm's configuration,
  Exit the simulator
  
## 🧠 How It Works
* **Forward Kinematics:** Uses the link lengths and joint angles to compute the position of each joint and the end-effector. This is visualized using a simple 2D plot.
* **Inverse Kinematics:** For 2-link arms, the program calculates joint angles to reach a target position (x, y) using geometric methods and trigonometry.
> Note: Inverse kinematics is limited to 2-link arms in the current version.

## 💡 Example Usage

```bash
Enter number of links (2 recommended): 2
Enter length of link 1: 10
Enter initial angle (in degrees) for joint 1: 45
Enter length of link 2: 7
Enter initial angle (in degrees) for joint 2: 30

Options:
1. Set joint angles
2. Move to position using inverse kinematics
3. Plot current arm configuration
4. Exit
Choose an option:
```

## 📁 File Structure

```
robot_arm_simulator.py       # Main program code
README.md                    # This file
```

## 🛠 Future Improvements

 * Add support for 3+ link inverse kinematics
 * Include animation support to simulate motion
 * GUI interface using PyQt or Tkinter
 * Export simulation data to CSV or JSON
 * Integrate with physics engines like PyBullet
