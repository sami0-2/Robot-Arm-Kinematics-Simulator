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
  * soem
