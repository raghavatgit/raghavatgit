<div align="center">
  <img src="assets/banner.svg?v=1790599722" alt="Raghav Goyal" width="100%" />
</div>

<br />

<div align="center">
  <a href="https://crag.web.app"><strong>Portfolio</strong></a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://contactraghav.web.app"><strong>3D Space Portal</strong></a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/raghav-goyal-linkd/"><strong>LinkedIn</strong></a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="mailto:goyalraghav1289@gmail.com"><strong>Email Direct</strong></a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://github.com/raghavatgit?tab=repositories"><strong>Repositories</strong></a>
</div>

<br />

---

### Executive Overview

Undergraduate computer science student at South Asian University ('29) specializing in native Windows desktop systems, zero-dependency spatial web architectures, and operating system internals. Engineering approach emphasizes minimal resident memory footprints, elimination of third-party framework overhead, and rigorous asymptotic complexity guarantees.

---

### What I Do: Engineering & Production Systems

#### 1. Windows Systems Latency, Performance & Debloater Architecture
- **[AnxiouslyOptimized](https://github.com/raghavatgit/AnxiouslyOptimized)**: Enterprise-grade Windows latency tuner, gaming performance optimizer, and system debloater built with native C# and Direct3D hardware-accelerated WPF.
- **Direct3D & WPF Architecture**: Standalone 275 KB zero-dependency binary with sub-50ms instant cold boot, responsive liquid-glass dark UI, 9 modular bento-grid feature tabs, and persistent theme states.
- **Kernel-Level Registry & Dispatcher Engine**: Dual-OS registry optimization engine supporting Windows 10 and Windows 11, hardware-accelerated GPU scheduling, system timer resolution tuning, DWM responsiveness, and automated AppX bloatware removal with safety whitelist verification.
- **Gaming & Android Emulator Acceleration**: Custom subsystem for BlueStacks 5 and MSI App Player unlocking 240 FPS via ASUS ROG Phone 2 profile emulation, mouse acceleration curve neutralization for drag headshots, and network packet pacing.
- **System Safety & Reversibility**: Built-in automated System Restore point creation, selective registry hive backups, and a 40-point automated deep validation test suite.
- **Instant Zero-Install Run**: Launch directly on any Windows machine via PowerShell with automated UAC elevation and zero local prerequisites:
  ```powershell
  irm https://raw.githubusercontent.com/raghavatgit/AnxiouslyOptimized/main/run.ps1 | iex
  ```
- **Actions**: [Inspect Architecture & Implementation ->](https://github.com/raghavatgit/AnxiouslyOptimized)

#### 2. Decentralized Disaster Emergency Mesh & IoT Hardware Systems
- **[Aegis-Raksha](https://github.com/raghavatgit/Aegis-Raksha)**: Decentralized disaster distress communication architecture engineered for infrastructure-collapsed zones.
- **Embedded RF Transceiver Firmware**: Direct C++ Arduino firmware for Semtech SX1276/SX1278 (868/915 MHz) transceivers implementing controlled multi-hop packet flooding, TTL hop limits, and in-memory ring-buffer de-duplication to eliminate broadcast storms.
- **Offline Mobile Client**: Cross-platform Flutter client communicating via Bluetooth Low Energy (BLE) GATT profiles to acquire background GPS coordinates, dispatch distress beacons, and trigger local audio sirens without cellular or internet connectivity.
- **Hardware Gateway Bridges**: Python and PowerShell serial bridges (`iot_usb_bridge.py`, `iot_usb_bridge.ps1`) streaming field node telemetry to cloud command centers.
- **Action**: [Inspect Architecture & Implementation ->](https://github.com/raghavatgit/Aegis-Raksha)

#### 3. GPS-Denied Autonomous Dead Reckoning Navigation & Inertial Odometry
- **[NavDrishti](https://github.com/raghavatgit/NavDrishti)**: Autonomous positioning and sensor fusion engine engineered for GPS-denied environments (tunnels, subterranean shafts, and GNSS-jammed theatres). Built for Smart India Hackathon (SIH 2026).
- **Inertial Machine Learning**: Temporal Convolutional Network (TCN) learning linear displacement and velocity directly from noisy 6-DOF IMU accelerometer and gyroscope vectors.
- **Multi-Sensor Kalman Filtering**: Extended Kalman Filter (EKF) combining wheel tick odometry, magnetometer heading reference, and Zero Velocity Updates (ZUPT) to prevent exponential integration drift.
- **Geospatial Visualization**: Leaflet.js engine rendering live vehicle trajectories, confidence ellipses, and ground-truth comparisons.
- **Action**: [Inspect Architecture & Implementation ->](https://github.com/raghavatgit/NavDrishti)

#### 4. Native Desktop Systems & Privacy Isolation
- **[StreamShield](https://github.com/raghavatgit/StreamShield)**: Lightweight Windows desktop utility engineered with Rust and Tauri that isolates sensitive application windows from screen capture pipelines (OBS, Discord, Zoom) in real time.
- **Kernel-Level Affinity**: Direct interop with Windows Win32 API via `SetWindowDisplayAffinity(hwnd, WDA_EXCLUDEFROMCAPTURE)` at the Desktop Window Manager (DWM) compositor level.
- **Resource Discipline**: Operates strictly within a sub-25 MB resident RAM footprint with an asynchronous, non-blocking IPC state bridge between the Rust core and the user interface.
- **Action**: [Inspect Architecture & Implementation ->](https://github.com/raghavatgit/StreamShield)

#### 5. Industrial IoT Telemetry & Agri-Tech Analytics
- **[Bitverse-Agrostat](https://github.com/raghavatgit/Bitverse-Agrostat)**: End-to-end industrial IoT telemetry pipeline streaming continuous soil nutrient data (NPK), ambient temperature, and moisture from ESP32 microcontrollers.
- **Streaming Pipeline**: Python FastAPI server and USB serial bridge dispatching high-frequency telemetry over WebSockets to predictive crop disease models.
- **Analytics Dashboard**: React 18, Tailwind CSS, and Vite analytics dashboard displaying real-time environmental trends and crop risk scores.
- **Action**: [Inspect Architecture & Implementation ->](https://github.com/raghavatgit/Bitverse-Agrostat)

#### 6. Spatial 3D Web & Interactive Interface Physics
- **[ContactMe](https://contactraghav.web.app)**: Interactive 3D spatial web environment calculating perspective matrix transformations driven by cursor velocity vectors.
- **Mathematical Rendering**: Pure CSS3 3D Matrix calculations executed inside a sub-1ms `requestAnimationFrame` loop, eliminating WebGL and Three.js runtime overhead entirely.
- **Zero-Bloat Delivery**: Complete client bundle compressed under 15 KB gzipped, deployed globally on Firebase edge hosting.
- **[Zenflow-3D](https://github.com/raghavatgit/Zenflow-3D)**: Deep focus spatial interface implementing multi-layered perspective planes and tactile physics.
- **Actions**: [Launch Interactive Portal ->](https://contactraghav.web.app) | [Inspect Source Code ->](https://github.com/raghavatgit/ContactMe) | [Explore Zenflow-3D ->](https://github.com/raghavatgit/Zenflow-3D)

#### 7. Audio Digital Signal Processing & Desktop Extensions
- **[vencord-ytm-player](https://github.com/raghavatgit/vencord-ytm-player)**: Embedded YouTube Music companion client extension for Vencord with real-time DSP audio normalization.
- **Dynamic Range Normalization**: Real-time logarithmic DSP curve preventing sudden volume spikes between music tracks.
- **IPC State Broadcast**: Persistent non-blocking communication channel synchronizing track metadata and state to Discord Rich Presence.
- **Ring Buffer Queue**: Low-latency memory queue management ensuring seamless playback resumption.
- **Action**: [Inspect Client Extension ->](https://github.com/raghavatgit/vencord-ytm-player)

#### 8. Civic Web Infrastructure & Component Systems
- **[Orbit-SmartCity](https://github.com/raghavatgit/Orbit-SmartCity)**: Modular municipal services and emergency dispatch portal built with React 18, Tailwind CSS, and Vite. Features componentized views for emergency alerts, transit routing, and municipal department directories.
- **Action**: [Inspect Web Architecture ->](https://github.com/raghavatgit/Orbit-SmartCity)

---

### What I Learn: Systems Research & Algorithmic Foundations

#### 1. Algorithmic Problem Solving & Data Structures
- **[dsa-patterns](https://github.com/raghavatgit/dsa-patterns)**: Over 100 production-grade algorithmic implementations in Rust, C++, and TypeScript.
- **Coverage**: Dynamic programming (state compression, bitmask DP), graph theory (Tarjan SCC, Dijkstra, topological sorting), monotonic queues, sliding windows, and bitwise manipulation.
- **Rigor**: Every solution is accompanied by formal asymptotic time and space complexity proofs, invariant analysis, and comprehensive unit tests.
- **Action**: [Explore Algorithmic Repository ->](https://github.com/raghavatgit/dsa-patterns)

#### 2. Operating Systems Internals & Systems Notes
- **[til: Today I Learned](https://github.com/raghavatgit/til)**: Over 110 structured engineering notes cataloging low-level computing architectures:
  - **Linux VFS Layer**: Inode lifecycle, dentry cache invalidation, page cache writeback flushing, file descriptor table mechanics.
  - **Storage Engines**: Log-Structured Merge (LSM) trees, SSTables, write amplification vs B+ Tree in-place updates.
  - **Memory Subsystems**: Virtual memory mapping, page table walks, slab allocators, copy-on-write (COW) semantics.
  - **Networking Stack**: TCP state machines, epoll event multiplexing, congestion control algorithms (CUBIC, BBR).
- **Action**: [Browse Systems Knowledge Base ->](https://github.com/raghavatgit/til)

#### 3. Academic Foundation & Theoretical Computer Science
- Department of Computer Science, South Asian University, New Delhi (Class of 2029).
- **[sau-cs-core](https://github.com/raghavatgit/sau-cs-core)**: Formal implementations of Design & Analysis of Algorithms (Matrix Chain Multiplication, Huffman Coding, Dijkstra, Floyd-Warshall, Bellman-Ford, Ford-Fulkerson Network Flow in C) and enterprise multi-tier Object-Oriented design patterns in Java.
- **Action**: [Inspect Academic Codebase ->](https://github.com/raghavatgit/sau-cs-core)

---

### Technical Stack & Tooling

| Domain | Core Technologies | Focus & Architectural Principles |
| :--- | :--- | :--- |
| **Low-Level Systems** | C#, C++, Rust, Win32 API, POSIX, WPF, Direct3D | Kernel hooks, Direct3D UI, OS latency tuning, memory safety, sub-25 MB RAM footprints. |
| **Embedded & IoT Mesh** | C++, ESP32, LoRa SX1276, BLE, UART, GATT | Multi-hop flood mesh protocols, packet de-duplication, RF link budgets, low-power telemetry. |
| **Robotics & Sensor Fusion** | Python, Kalman Filtering (EKF), TCN, Leaflet, Kotlin | GPS-denied dead reckoning, inertial odometry, Zero Velocity Updates (ZUPT). |
| **Spatial & Front-End Web** | TypeScript, JavaScript (ES6+), React, Next.js, HTML5, CSS3 | Pure CSS3 3D Matrix mathematics, sub-1ms RAF render loops, zero framework bloat. |
| **Audio & Native Runtimes** | Web Audio API, Tauri, Node.js, Webpack | Real-time logarithmic DSP dynamics, Discord RPC synchronization, desktop sandboxing. |
| **Cloud & DevOps** | Google Cloud Platform (GCP), Firebase, Git, GitHub Actions | Edge CDN hosting, CI/CD automated telemetry pipelines, Linux environments. |

---

### Open Source Repositories

| Repository | Focus | Primary Stack | Architecture Summary |
| :--- | :--- | :--- | :--- |
| **[Aegis-Raksha](https://github.com/raghavatgit/Aegis-Raksha)** | Disaster Mesh Network | C++, ESP32, Flutter, LoRa, BLE | Multi-hop LoRa SX1276 emergency network bridging offline BLE mobile clients in disaster zones. |
| **[NavDrishti](https://github.com/raghavatgit/NavDrishti)** | Autonomous Navigation | Python, EKF, TCN, Leaflet, Kotlin | GPS-denied dead reckoning navigation engine fusing IMU odometry and Kalman filtering (SIH 2026). |
| **[AnxiouslyOptimized](https://github.com/raghavatgit/AnxiouslyOptimized)** | Windows Performance & Debloater | C#, WPF, Direct3D, PowerShell | Standalone 275 KB latency optimizer with sub-50ms startup, dual-OS registry tuning, and gaming booster. |
| **[Bitverse-Agrostat](https://github.com/raghavatgit/Bitverse-Agrostat)** | Industrial Agri-IoT | C++, ESP32, Python, FastAPI, React | Real-time soil nutrient telemetry pipeline with crop disease predictive models. |
| **[sau-cs-core](https://github.com/raghavatgit/sau-cs-core)** | Academic CS Foundations | C, Java | South Asian University theoretical algorithms (Ford-Fulkerson, MCM) and enterprise Java OOP. |
| **[dsa-patterns](https://github.com/raghavatgit/dsa-patterns)** | Algorithms | Rust, C++, TypeScript | 100+ algorithmic solutions with formal complexity proofs and test suites. |
| **[til](https://github.com/raghavatgit/til)** | Systems Research | Markdown, Systems Architecture | 110+ technical notes on Linux VFS, storage engines, and kernel subsystems. |
| **[StreamShield](https://github.com/raghavatgit/StreamShield)** | Desktop Security | Rust, Tauri, Win32 API, React | Windows capture isolation masking sensitive application windows in real time. |
| **[Orbit-SmartCity](https://github.com/raghavatgit/Orbit-SmartCity)** | Civic Infrastructure Web | React 18, Tailwind CSS, Vite | Modular municipal portal for emergency dispatch, transit schedules, and public services. |
| **[ContactMe](https://github.com/raghavatgit/ContactMe)** | Spatial 3D Web | Vanilla JavaScript, CSS3 Matrix | Cursor-velocity physics portal with sub-1ms RAF loop and zero dependencies. |
| **[vencord-ytm-player](https://github.com/raghavatgit/vencord-ytm-player)** | Audio DSP | TypeScript, React, Web Audio API | YouTube Music Vencord client with logarithmic DSP normalization and Discord RPC. |
| **[discord-ptb-palette](https://github.com/raghavatgit/discord-ptb-palette)** | Windows Systems Utility | Python, WinAPI COM, Shell | Windows desktop shortcut automation, launch parameter mutation, and icon synthesis. |

---

### Live Telemetry & Engineering Activity

<div align="center">
  <img src="assets/telemetry.svg?v=1790599722" alt="Telemetry Dashboard" width="100%" />
</div>

<br />

| Metric | Telemetry Count | Focus Domain |
| :--- | :--- | :--- |
| **Annual Activity** | 910+ Contributions (Active Streak) | Algorithmic Problem Solving & Systems Development |
| **Problem Solutions** | 210+ Production-Grade Solutions | Rust, C++, TypeScript ([dsa-patterns](https://github.com/raghavatgit/dsa-patterns)) |
| **Systems & Architecture** | 100+ Technical Engineering Notes | Linux VFS, Distributed Systems, Networking ([til](https://github.com/raghavatgit/til)) |
| **Active Codebases** | 18 Public Repositories | Embedded IoT, Autonomous Navigation, Systems Utilities |

---

### Freelance Services & Client Solutions

- **Native Desktop App & Systems Optimization**: Building high-efficiency desktop utilities, Windows latency optimizers, and lightweight tools using C#, WPF (Direct3D), Rust, and Tauri with minimal resource consumption.
- **Full-Stack Web Design & Prototyping**: Engineering bespoke, modern web applications, high-converting product landing pages, and interactive 3D spatial web experiences with zero bloated dependencies.
- **End-to-End MVP Delivery**: Transforming product ideas into deployed, fully functional prototypes with automated CI/CD and edge cloud deployment on GCP and Firebase.

---

### Contact & Collaboration

Whether you are looking for a responsive full-stack web application, a custom native desktop utility, or an end-to-end prototype:

- **Portfolio**: [crag.web.app](https://crag.web.app)
- **Interactive Space**: [contactraghav.web.app](https://contactraghav.web.app)
- **LinkedIn**: [linkedin.com/in/raghav-goyal-linkd](https://www.linkedin.com/in/raghav-goyal-linkd/)
- **Email**: [goyalraghav1289@gmail.com](mailto:goyalraghav1289@gmail.com)
- **Location**: New Delhi, India

<br />

<div align="center">
  <img src="assets/footer.svg?v=1790599722" alt="Footer Banner" width="100%" />
</div>
