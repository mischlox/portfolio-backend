## PROFILE

**Software Engineer (M.Sc.)** specialized in **C++ and Python** in the areas of **Embedded Systems, Real-Time Applications, Computer Vision, Deep Learning, and Sensor Fusion**.

Experience in developing high-performance software components for **AI-based perception systems, autonomous systems, and embedded hardware platforms**. Focus on **Computer Vision pipelines, Deep Learning deployment on edge devices, multimodality (Camera–LiDAR Fusion)**, and **robust software architectures for sensor-based systems**.

Strong orientation towards **high-performance C++/Python systems on Linux**, reproducible research pipelines, and **scalable AI systems for real-world applications** in industry and research.

---

# SKILLS

### Programming Languages

* C++
* Python
* Java
* Bash
* JavaScript

### Tools & Platforms

* Linux
* CMake
* Git
* Docker
* Buildroot
* VS Code
* Atlassian Suite (Jira, Confluence, Bitbucket)

### Frameworks & Libraries

* ROS2
* OpenCV
* Qt
* GoogleTest
* PyTest
* OpenPCDet
* PyTorch
* Open3D
* NumPy

### AI / Computer Vision

* Object Detection
* Tiny Object Detection
* Monocular Depth Estimation
* Multimodal Sensor Fusion
* Camera–LiDAR Fusion
* Pseudo-Labeling
* Dataset Annotation & Augmentation
* Domain Adaptation
* Embedded AI Deployment
* Model Optimization (Quantization, Pruning)

### Embedded & Systems

* ARM (Jetson)
* FPGA / GPU Inference Platforms
* Nvidia TensorRT
* Xilinx Vitis AI
* Embedded Linux
* Buildroot
* Edge AI Systems

### Concepts

* Software Architecture
* Test-Driven Development
* Real-Time Systems
* Sensor Fusion
* Distributed Systems
* Agile Software Development (Scrum)

### Languages

* German (Native)
* English (Fluent)
* Russian (Basic knowledge)

---

# EDUCATION

## Master of Science – Robotics, Cognition and Intelligence

**Technical University of Munich**
10/2022 – 09/2025

Focus on **AI-based perception for autonomous systems** and intelligent robotics.

### Focus Areas

* Computer Vision
* 3D Reconstruction
* Object Detection and Segmentation
* Sensor Fusion
* Machine Learning
* Real-Time Systems
* Autonomous Driving

---

## Master's Thesis

### Multimodal Pseudo-Labeling for 3D Object Detection in Autonomous Driving

**Grade: 1.0**

Development of a pipeline to improve **3D object detection with limited or noisy LiDAR annotations** by leveraging additional camera information.

### Contributions

* Development of a **camera-assisted pseudo-labeling pipeline** combining:
  * monocular depth estimation
  * 2D detection and segmentation
  * LiDAR-based 3D detection

* Generation of **pseudo-LiDAR point clouds from monocular images** using state-of-the-art depth estimation and depth correction.

* Implementation of **projection- and segmentation-based label refinement**, updating 3D classes using 2D semantic evidence.

* Integration and extension of **OpenPCDet and nuScenes**, including:
  * custom evaluation metrics (e.g. range-based metrics)
  * efficient annotation processing.

* Analysis of **domain gaps between datasets** and evaluation of:
  * Semi-Supervised Learning
  * Unsupervised Domain Adaptation.

* Demonstration of **measurable improvements in detection quality and label consistency** through multimodal supervision with reduced manual labeling effort.

Strong focus on **modular research software, reproducible experiments, and systematic evaluation under realistic autonomous driving scenarios**.

---

## Bachelor of Science – Computer Science / Software Engineering

**Aalen University of Applied Sciences**
10/2018 – 09/2022

Focus areas:

* Software Architecture
* Clean Code
* Software Testing
* Distributed Systems
* Embedded Systems
* Mobile Development

---

## Bachelor's Thesis & Publication

### Thesis

**Evaluation and Optimization of Deep-Learning based Object Detection on Embedded Inference Hardware from Xilinx and Nvidia**
**Grade: 1.3**

### Publication

*A Framework for Benchmarking Real-Time Embedded Object Detection*
**DAGM GCPR 2022**

---

# WORK EXPERIENCE

## Software Engineer (Part-Time)

**JOOLS GmbH – Heubach**
10/2025 – Present

Part-time role focused on **practical software solutions for the automation and digitalization of a retail business**.

### Focus Areas

* Development of tools for **automating daily business processes**
* Digitalization of internal workflows
* Development of cost-effective IT systems for small businesses

### Key Contributions

#### Digital Signage System

Development of a **Raspberry Pi-based system for managing advertising displays** across multiple branches.

Features:

* centralized content control
* remote updates
* monitoring

Remote management via **Tailscale**.

---

#### Employee Time Tracking System

Design and implementation of a **full-stack desktop application** for employee time tracking.

Features:

* login system
* working time tracking
* admin dashboard
* vacation and sick leave management
* automated **PDF reports for payroll**

Technologies:

Python, SQLite, JavaScript

---

#### Inventory & Sales Analysis Tools

Development of scripts for **analyzing incoming goods and sales data** to:

* support inventory planning
* generate automated order suggestions.

---

#### Infrastructure & IT Support

* Network setup
* Device installation
* Setup of **IP camera systems**
* Support with system configuration and IT security.

---

#### Workflow Automation

Development of small **Python and Bash utilities** to:

* reduce manual data entry
* automate internal workflows
* minimize sources of error.

---

## Working Student – Perception & Sensor Systems

**HAT.tec GmbH – Neubiberg**
10/2022 – 10/2024

Development and integration of modular **C++/Python components for sensor and image processing systems on Linux**.

**ROS2** was used to **structure and orchestrate distributed data flows between sensors and algorithms**.

---

### Focus Areas

* Sensor and image processing systems
* Distributed ROS2 architectures
* Tiny Object Detection
* Deployment of deep learning models on target hardware

---

### Key Contributions

#### Object Detection Pipeline

Design, training, and deployment of optimized **state-of-the-art tiny object detection models** (e.g. for aircraft detection).

Models were **adapted to specific sensor data and domain requirements**.

---

#### Dataset Management & Annotation

* Management of large datasets
* Annotation of training data
* Data augmentation
* Preparation of training and evaluation data.

---

#### Sensor Processing

Development of modular **C++ and Python components within ROS2 applications** for efficient processing and analysis of sensor data streams.

---

#### Refactoring & Performance Optimization

Execution of extensive **refactoring of existing software modules** to:

* increase performance
* reduce system latency
* improve maintainability.

---

#### Cross-Platform Deployment

Integration and testing of software components on various target platforms:

* ARM (Jetson)
* x86
* customer-specific hardware.

Responsibility for **hardware interfacing and integration**.

---

#### Quality Assurance

Development of automated tests using:

* **GoogleTest (C++)**
* **PyTest (Python)**

to ensure **code robustness and system stability**.

---

## Intern / Working Student / Bachelor's Thesis

### Computer Vision & Image Processing

**HENSOLDT Optronics GmbH – Oberkochen**
09/2020 – 09/2022

Focus on **benchmarking and deployment of deep learning object detectors on embedded hardware (edge devices)**.

---

### Focus Areas

* Edge AI
* Embedded Deep Learning
* Benchmarking of inference hardware
* Cross-platform model deployment

---

### Key Contributions

#### Generic Benchmarking Framework

Design and implementation of a **lightweight framework** to connect a host evaluation PC with multiple embedded systems.

---

#### Comprehensive Evaluation

Separation of:

* data distribution
* evaluation logic

to simultaneously measure:

* accuracy
* runtime
* energy consumption

without affecting the target hardware.

---

#### Optimization & Cross-Platform Deployment

Comparison and use of **vendor-specific optimization pipelines**:

* Nvidia TensorRT (Jetson AGX Xavier)
* Xilinx Vitis AI (ZCU104)

Analysis of **accuracy vs. speed trade-offs** through:

* quantization
* pruning.

---

#### Embedded Systems Implementation

* Development of target software in **C++**
* Configuration of **embedded Linux environments**
* Deployment and verification of deep learning models on **FPGA and GPU platforms**.

---

# PROJECTS

## InfluxSense – Embedded People Counter

github.com/mischlox/influxsense

Self-hosted foot-traffic counter for small retail businesses running on a Raspberry Pi with a VL53L5CX Time-of-Flight sensor. No cloud, no camera, ~€30 in hardware.

Features:

* 8×8 ToF depth grid processed at 20 Hz with FSM-based entry/exit detection
* Hardware abstraction layer (`ISensor`) with mock for host-side development and testing
* Multithreaded producer/consumer pipeline with fixed-capacity ring buffer (`std::array`, no heap allocation after startup)
* SQLite persistence with CTE-based hourly aggregation
* Live web dashboard over HTTP with Server-Sent Events — accessible from any device on the local network
* aarch64 cross-compilation, automated deploy via rsync + systemd

Technologies:

C++17, CMake, Conan 2, SQLite, GoogleTest, Raspberry Pi

---

## Portfolio Chat API

github.com/mischlox/portfolio-backend

Backend for a portfolio with an integrated **AI assistant**.

Features:

* RAG-based chatbot for questions about professional background
* Vector database for semantic search
* State machine-based multi-step logic
* Integrated email service.

Technologies:

Python, FastAPI, LangGraph, ChromaDB, OpenAI API, Gemini API

---

## Company Research Agent

github.com/mischlox/company-researcher

Tool for **automated company research for interview preparation**.

Features:

* Generation of search queries
* Web research
* Automatic creation of reports and interview questions.

Technologies:

Python, Google ADK, Gradio, Gemini API, Pydantic, MLflow

---

## Face Touching Detector

github.com/mischlox/face-touching-detector

C++ desktop application for **real-time detection of face touching**.

Technologies:

* YOLOv5m
* Libtorch C++
* Qt GUI
* CUDA

---

## Augmented Reality Object Recognition App

github.com/mischlox/AR-App-Object-Recognition

Android app for **real-time object recognition and extension of an ML model directly on the smartphone**.

Features:

* Continual Learning
* On-Device Training
* Offline Inference

Technologies:

Java, TensorFlow Lite, Android SDK, MobileNetV2

---

## ROS2 Scan Table Manager

github.com/mischlox/ros2-scan-table-cell

Simulation of an **automated pick-and-place inspection cell**.

A central state machine node coordinates:

* robot movements
* barcode scans
* object validations

via asynchronous ROS2 services.

---

## PiSignage – Low Cost Digital Signage System

github.com/mischlox/pisignage

Self-hosted digital signage system on Raspberry Pi.

Features:

* Remote device management
* Cost-effective alternative to commercial solutions
* Productive use on multiple displays.

Technologies:

Python, Flask, Electron, Node.js, Raspberry Pi, Tailscale.