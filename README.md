<div align="center">
  <img src="assets/banner.svg?v=1790525827" alt="Raghav Goyal" width="100%" />
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

#### 1. Native Desktop Systems & Privacy Isolation
- **[StreamShield](https://github.com/raghavatgit/StreamShield)**: Lightweight Windows desktop utility engineered with Rust and Tauri that isolates sensitive application windows from screen capture pipelines (OBS, Discord, Zoom) in real time.
- **Kernel-Level Affinity**: Direct interop with Windows Win32 API via `SetWindowDisplayAffinity(hwnd, WDA_EXCLUDEFROMCAPTURE)` at the Desktop Window Manager (DWM) compositor level.
- **Resource Discipline**: Operates strictly within a sub-25 MB resident RAM footprint with an asynchronous, non-blocking IPC state bridge between the Rust core and the user interface.
- **Action**: [Inspect Architecture & Implementation ->](https://github.com/raghavatgit/StreamShield)

#### 2. Spatial 3D Web & Interactive Interface Physics
- **[ContactMe](https://contactraghav.web.app)**: Interactive 3D spatial web environment calculating perspective matrix transformations driven by cursor velocity vectors.
- **Mathematical Rendering**: Pure CSS3 3D Matrix calculations executed inside a sub-1ms `requestAnimationFrame` loop, eliminating WebGL and Three.js runtime overhead entirely.
- **Zero-Bloat Delivery**: Complete client bundle compressed under 15 KB gzipped, deployed globally on Firebase edge hosting.
- **[Zenflow-3D](https://github.com/raghavatgit/Zenflow-3D)**: Deep focus spatial interface implementing multi-layered perspective planes and tactile physics.
- **Actions**: [Launch Interactive Portal ->](https://contactraghav.web.app) | [Inspect Source Code ->](https://github.com/raghavatgit/ContactMe) | [Explore Zenflow-3D ->](https://github.com/raghavatgit/Zenflow-3D)

#### 3. Audio Digital Signal Processing & Desktop Extensions
- **[vencord-ytm-player](https://github.com/raghavatgit/vencord-ytm-player)**: Embedded YouTube Music companion client extension for Vencord with real-time DSP audio normalization.
- **Dynamic Range Normalization**: Real-time logarithmic DSP curve preventing sudden volume spikes between music tracks.
- **IPC State Broadcast**: Persistent non-blocking communication channel synchronizing track metadata and state to Discord Rich Presence.
- **Ring Buffer Queue**: Low-latency memory queue management ensuring seamless playback resumption.
- **Action**: [Inspect Client Extension ->](https://github.com/raghavatgit/vencord-ytm-player)

#### 4. Commercial Web & Contract MVP Delivery
- Delivering production-ready web applications, high-converting landing pages, and interactive prototypes deployed on Google Cloud Platform and Firebase edge infrastructure with automated CI/CD pipelines.

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

#### 3. Academic Foundation
- Department of Computer Science, South Asian University, New Delhi (Class of 2029).

---

### Technical Stack & Tooling

| Domain | Core Technologies | Focus & Architectural Principles |
| :--- | :--- | :--- |
| **Low-Level Systems** | C++, Rust, Win32 API, POSIX | Kernel capture hooks, IPC channels, memory safety, sub-25 MB RAM footprints. |
| **Spatial & Front-End Web** | TypeScript, JavaScript (ES6+), React, Next.js, HTML5, CSS3 | Pure CSS3 3D Matrix mathematics, sub-1ms RAF render loops, zero framework bloat. |
| **Audio & Native Runtimes** | Web Audio API, Tauri, Node.js, Webpack | Real-time logarithmic DSP dynamics, Discord RPC synchronization, desktop sandboxing. |
| **Cloud & DevOps** | Google Cloud Platform (GCP), Firebase, Git, GitHub Actions | Edge CDN hosting, CI/CD automated telemetry pipelines, Linux environments. |

---

### Open Source Repositories

| Repository | Focus | Primary Stack | Architecture Summary |
| :--- | :--- | :--- | :--- |
| **[dsa-patterns](https://github.com/raghavatgit/dsa-patterns)** | Algorithms | Rust, C++, TypeScript | 100+ algorithmic solutions with formal complexity proofs and test suites. |
| **[til](https://github.com/raghavatgit/til)** | Systems Research | Markdown, Systems Architecture | 110+ technical notes on Linux VFS, storage engines, and kernel subsystems. |
| **[StreamShield](https://github.com/raghavatgit/StreamShield)** | Desktop Security | Rust, Tauri, Win32 API, React | Windows capture isolation masking sensitive application windows in real time. |
| **[ContactMe](https://github.com/raghavatgit/ContactMe)** | Spatial 3D Web | Vanilla JavaScript, CSS3 Matrix | Cursor-velocity physics portal with sub-1ms RAF loop and zero dependencies. |
| **[vencord-ytm-player](https://github.com/raghavatgit/vencord-ytm-player)** | Audio DSP | TypeScript, React, Web Audio API | YouTube Music Vencord client with logarithmic DSP normalization and Discord RPC. |
| **[Zenflow-3D](https://github.com/raghavatgit/Zenflow-3D)** | Spatial Focus | JavaScript, CSS3 Perspectives | Kinetic motion focus environment utilizing multi-layered perspective planes. |
| **[FoodStaticWebs](https://github.com/raghavatgit/FoodStaticWebs)** | Commercial Web | HTML5, CSS3 Grid, JavaScript | High-performance culinary templates with fluid responsive layouts. |

---

### Live Telemetry & Engineering Activity

<div align="center">
  <img src="assets/telemetry.svg?v=1790525827" alt="Telemetry Dashboard" width="100%" />
</div>

<br />

| Metric | Telemetry Count | Focus Domain |
| :--- | :--- | :--- |
| **Annual Activity** | 886+ Contributions (Active Streak) | Algorithmic Problem Solving & Systems Development |
| **Problem Solutions** | 100+ Production-Grade Solutions | Rust, C++, TypeScript ([dsa-patterns](https://github.com/raghavatgit/dsa-patterns)) |
| **Systems & Architecture** | 110+ Technical Engineering Notes | Linux VFS, Distributed Systems, Networking ([til](https://github.com/raghavatgit/til)) |
| **Active Codebases** | 12 Public Repositories | Desktop Utilities, Web Audio DSP, Spatial 3D Web |

---

### Freelance Services & Client Solutions

- **Full-Stack Web Design & Prototyping**: Engineering bespoke, modern web applications, high-converting product landing pages, and interactive 3D spatial web experiences with zero bloated dependencies.
- **Native Desktop App Development**: Building high-efficiency desktop utilities and lightweight tools using Rust, Tauri, and TypeScript with minimal resource consumption.
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
  <img src="assets/footer.svg?v=1790525827" alt="Footer Banner" width="100%" />
</div>
