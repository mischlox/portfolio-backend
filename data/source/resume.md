# Resume

## SHORT PROFILE

**Software Engineer** (M.Sc.) specializing in **C++ and Python** in the fields of **Embedded Systems, Real-Time Applications, Computer Vision**, **Deep Learning**, and **Sensor Fusion**. Profound knowledge in developing complex software components for the defense and automotive industries.

---

## SKILLS

**Programming Languages:** C++, Python, Java, Bash, JavaScript

**Tools & Platforms:** Linux, CMake, Git, Docker, Buildroot, VS Code, Atlassian Suite (Jira, Confluence, Bitbucket)

**Frameworks & Libraries:** GoogleTest, PyTest, Qt, OpenCV

**Concepts:** Agile Software Development (Scrum), Software Architecture & UML, Test-Driven Development, Embedded Systems, Real-Time Applications, Sensor Fusion

**Languages:** German (Native), English (Fluent), Russian (Basic knowledge)

---

## EDUCATION

### **Master of Science – Robotics, Cognition and Intelligence**

* Technical University of Munich
* 10/2022 – 09/2025
* **Focus:** Intelligent robotic systems, **AI-driven perception**, learning-based decision making, human-robot interaction (e.g., autonomous driving).
* **Specialization:** **Computer Vision & Perception** (3D reconstruction, object detection, segmentation), **Sensor Fusion**, **Machine Learning** (optimization, statistical learning), **Real-Time Systems**, and classical robotics.

### **Bachelor of Science – Informatics / Software Engineering**

* Aalen University
* 10/2018 – 09/2022
* **Focus:** Systematic software development, clean code principles, and robust, scalable software systems.
* **Specialization:** **Software Architecture & Design**, **Software Quality & Testing**, Project Management, Distributed Systems, and **Embedded & Mobile Development**.

---

## PROFESSIONAL EXPERIENCE

### Actively Seeking | Full-Time Software Engineer Roles

* 10/2025 – Present
* **Current Status:** Currently unemployed, searching for jobs. Actively on the job market, seeking full-time **Software Engineer** roles with a focus on **Computer Vision, AI, and Embedded Systems (C++/Python)**.
* **Continuous Development:** Concentrating on advanced personal projects (like this portfolio website) to explore and implement the latest State-of-the-Art (SOTA) technologies, including:
    * **Agentic AI Systems:** Deepening knowledge in **Multi-Agent Architecture** for complex data orchestration and research automation.

### Master Thesis | TUM Institute of Automotive Technology, Garching
* 11/2024 – 06/2025
* **Multimodal Pseudo-Labeling for 3D Object Detection in Autonomous Driving** (Grade: **1.0**)
* **Contributions:**
    * Developed a **camera-supported pseudo-labeling pipeline** combining monocular depth estimation, 2D detection/segmentation, and LiDAR-based 3D detection.
    * Generated **pseudo-LiDAR point clouds** from monocular images and implemented **projection- and segmentation-based label refinement** using 2D semantic evidence.
    * Integrated and extended **OpenPCDet and nuScenes** for custom evaluation (e.g., range-based metrics).
    * Analyzed domain gaps and evaluated semi-supervised and unsupervised adaptation strategies, achieving measurable **improvements in detection quality and label consistency**.
* *Technologies:* Python, PyTorch, OpenMMLab, OpenCV, Open3D, NumPy, Docker, Git, LaTeX, VS Code.

### Working Student – Perception & Sensor Systems | HAT.tec GmbH, Neubiberg
* 10/2022 – 10/2024
* **Focus:** Developing and integrating modular **C++/Python components** for sensor/image processing systems using **ROS2** for distributed data flow. Specialization in **tiny object detection** deployment.
* **Key Contributions:**
    * Designed, trained, and deployed optimized **State-of-the-Art Tiny Object Detection** models (e.g., for aircraft recognition) tailored for specific sensor data.
    * Developed modular **C++ and Python components** using **ROS2** for efficient sensor data processing and analysis.
    * Conducted major **refactoring** of existing software modules to significantly improve performance, reduce latency, and increase long-term maintainability.
    * Integrated and tested software components on diverse target systems (**ARM (Jetson), x86**), managing hardware connection and interfacing.
    * Implemented robust and automated testing frameworks using **GoogleTest (C++)** and **PyTest (Python)**.
    * Supported Requirements Engineering Team in writing test cases and performing system tests.
* *Technologies:* C++, Python, ROS2, Qt, OpenCV, CMake, Conan, GoogleTest, Linux, Docker, Git.

### Intern / Working Student / Bachelor Thesis – Computer Vision & Image Processing | HENSOLDT Optronics GmbH, Oberkochen
* 09/2020 – 09/2022
* **Focus:** Benchmarking and efficient deployment of deep neural network object detectors on embedded hardware (edge devices).
* **Bachelor Thesis:** *“Evaluation and Optimization of Deep-Learning based Object Detection on Embedded Inference Hardware from Xilinx and Nvidia”*. Grade: **1.3**
* **Publication:** *A Framework for Benchmarking Real-Time Embedded Object Detection, DAGM GCPR 2022*.
* **Key Contributions:**
    * Designed and implemented a novel, lightweight **Generic Benchmarking Framework** to connect a host evaluation PC with multiple embedded target devices, separating data distribution and evaluation for non-intrusive measurement of accuracy, runtime, and power consumption.
    * Utilized and compared vendor-specific optimization pipelines (**Nvidia TensorRT for Jetson AGX Xavier, Xilinx Vitis AI for ZCU104**) and applied techniques like quantization and pruning.
    * Implemented the target **C++ software** and configured **Embedded Linux environments (Buildroot)** for direct deployment and verification of Deep Learning models on FPGA/GPU platforms.
* *Technologies:* C++, CMake, Buildroot, Python, Docker, OpenVino, Qt, Linux, TensorRT, GStreamer.

---

## PROJECTS

### Company Research Agent [[github.com/mischlox/company-researcher](https://github.com/mischlox/company-researcher)]

* Tool for **automated company research**, optimized for job interview preparation.
* **Orchestration of agents** for generating search queries (Search Planning), conducting web searches (Automated Web Searches), and compiling reports and interview questions.
* Implemented with the **Google ADK** (Agent Development Kit) and interactive interface using **Gradio**.
* Focus on **Multi-Agent Architecture** and leveraging LLMs for data-driven analysis and reporting.
* *Technologies:* Python, Google ADK, Gradio, Gemini API, Pydantic, MLflow.

### Face Touching Detector [[github.com/mischlox/face-touching-detector](https://www.google.com/search?q=https://github.com/mischlox/face-touching-detector)]

* Desktop app in **C++** for **real-time detection** of face touches by detecting the overlap of hands and faces.
* Implementation of **YOLOv5m model inference** using **Libtorch C++** for high performance.
* Focus on **modular architecture** (Detector Interface), visualization with **Qt5** GUI, and simplified deployment via **Docker**.
* *Technologies:* C++, Libtorch, Qt, Docker, CUDA, YOLOv5.

### Augmented Reality Object Recognition App [[github.com/mischlox/AR-App-Object-Recognition](https://www.google.com/search?q=https://github.com/mischlox/AR-App-Object-Recognition)]

* **Android app in Java** for **real-time object recognition** and learning directly with the smartphone camera.
* Core functionality based on **Continual Learning** (Transfer Learning) to expand a pre-trained **MobilenetV2 model** with new objects.
* All processing (training and inference) is performed **offline on the device** (On-Device Processing) without external server connection.
* The model was extended with a configurable Softmax layer.
* *Technologies:* Java, TensorFlow Lite, Android SDK, MobilenetV2.

### Employee Time Tracking System

* Desktop tool with login, time tracking, admin dashboard, target/actual hours, vacation & sick leave management, PDF export.
* Productive use in 3 supermarket branches.
* *Technologies:* Python, SQLite, JavaScript, Eel, HTML, CSS.
