<div align="center">
  <img src="assets/banner.svg?v=5" alt="Raghav Goyal" width="100%" />
</div>

<br />

<div align="center">
  <a href="https://crag.web.app"><img src="assets/btn-portfolio.svg?v=5" height="34" alt="Portfolio" /></a>
  &nbsp;
  <a href="https://contactraghav.web.app"><img src="assets/btn-contact.svg?v=5" height="34" alt="3D Contact Portal" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/raghav-goyal-linkd/"><img src="assets/btn-linkedin.svg?v=5" height="34" alt="LinkedIn" /></a>
  &nbsp;
  <a href="mailto:goyalraghav1289@gmail.com"><img src="assets/btn-email.svg?v=5" height="34" alt="Email Inquiries" /></a>
</div>

<br />

---

### Engineering Profile & Focus

```typescript
interface SoftwareEngineer {
  name: "Raghav Goyal";
  role: "Aspiring Software Engineer | Freelance Full-Stack Developer";
  institution: "South Asian University ('29)";
  location: "New Delhi, India";
  specialties: [
    "3D Spatial Interfaces & Web Design",
    "Lightweight Native Desktop Utilities",
    "Algorithmic Problem Solving & Systems"
  ];
  principles: [
    "Zero unnecessary dependencies",
    "Sub-25 MB desktop resident memory footprint",
    "Micro-interaction ergonomics and sub-1ms render loops"
  ];
  availability: "Available for Contract MVP Delivery & Freelance Projects";
}
```

---

### Technology Stack & Architecture

<div align="center">
  <p>
    <strong>Core Languages</strong><br />
    <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" height="28" alt="C++" />
    <img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" height="28" alt="Rust" />
    <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" height="28" alt="TypeScript" />
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" height="28" alt="JavaScript" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" height="28" alt="Python" />
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" height="28" alt="HTML5" />
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" height="28" alt="CSS3" />
  </p>
  <p>
    <strong>Frontend & Native Systems</strong><br />
    <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" height="28" alt="React" />
    <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" height="28" alt="Next.js" />
    <img src="https://img.shields.io/badge/Tauri-24C8DB?style=for-the-badge&logo=tauri&logoColor=black" height="28" alt="Tauri" />
    <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" height="28" alt="Windows" />
    <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" height="28" alt="Linux" />
  </p>
  <p>
    <strong>Cloud, Databases & Tooling</strong><br />
    <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" height="28" alt="Google Cloud" />
    <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" height="28" alt="Firebase" />
    <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" height="28" alt="Node.js" />
    <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" height="28" alt="Git" />
  </p>
</div>

<br />

---

### Featured Architectures & Case Studies

<div align="center">
  <a href="https://contactraghav.web.app"><img src="assets/card-contactme.svg?v=5" width="48%" alt="ContactMe 3D Spatial Portal" /></a>
  &nbsp;
  <a href="https://github.com/raghavatgit/StreamShield"><img src="assets/card-streamshield.svg?v=5" width="48%" alt="StreamShield Privacy Isolation" /></a>
</div>

<br />

#### 1. [ContactMe | 3D Spatial Web Experience](https://contactraghav.web.app)
Interactive personal web portal calculating real-time cursor velocity and perspective transforms without third-party graphics engines.

- **Dynamic Cursor Physics**: Sub-1ms requestAnimationFrame render loop tracking mouse velocity vectors in real time.
- **CSS3 Matrix3D Calculations**: Pure mathematical perspective transformations eliminating Three.js and WebGL overhead.
- **Zero-Bloat Client Delivery**: Compressed under 15 KB gzipped footprint with zero external dependencies.
- **Production Edge Hosting**: Deployed globally on Firebase hosting at [contactraghav.web.app](https://contactraghav.web.app).

**Stack**: Vanilla ES6+, CSS3 3D Matrix, Firebase Edge Hosting  
**Actions**: [Launch Interactive Space ->](https://contactraghav.web.app) | [Inspect Source Repository ->](https://github.com/raghavatgit/ContactMe)

<br />

#### 2. [StreamShield | Native Windows Privacy Isolation](https://github.com/raghavatgit/StreamShield)
Lightweight Windows utility isolating sensitive application windows from OBS, Discord, and screen recording pipelines in real time.

- **Kernel-Level Capture Affinity**: Hooks Windows `SetWindowDisplayAffinity` API (`WDA_EXCLUDEFROMCAPTURE`) to mask target windows cleanly.
- **Selective Window Masking**: Automatically shields credentials, private chats, and sensitive apps while streaming.
- **Low-Footprint Architecture**: Built with Rust and Tauri, operating under a 25 MB resident RAM footprint.
- **Asynchronous IPC Bridge**: Non-blocking message channel communicating window states between the Rust core and React interface.

**Stack**: Rust, Tauri, Win32 API, React, TypeScript  
**Actions**: [Inspect Architecture & Implementation ->](https://github.com/raghavatgit/StreamShield)

<br />

#### 3. [vencord-ytm-player | Persistent Desktop Audio Client](https://github.com/raghavatgit/vencord-ytm-player)
Embedded YouTube Music companion client for Vencord with DSP audio normalization and Discord Rich Presence synchronization.

- **Logarithmic Audio DSP**: Real-time dynamic range normalization preventing sudden decibel spikes between tracks.
- **IPC Discord Synchronization**: Persistent non-blocking communication channel mirroring track metadata to Discord RPC.
- **Ring Buffer Queue Management**: Low-latency track caching ensuring smooth playback resumption.
- **Minimal System Overhead**: Lightweight background daemon footprint running inside the client sandbox.

**Stack**: TypeScript, React, Web Audio API, Webpack, Discord RPC  
**Actions**: [Inspect Client Extension ->](https://github.com/raghavatgit/vencord-ytm-player)

---

### Open Source Repositories & Knowledge Base

| Project | Category | Stack | Overview | Action |
| :--- | :--- | :--- | :--- | :--- |
| **[dsa-patterns](https://github.com/raghavatgit/dsa-patterns)** | Algorithms | Rust, C++, TypeScript | 100+ production-grade algorithmic solutions with formal complexity proofs and unit test harnesses. | [Explore Codebase ->](https://github.com/raghavatgit/dsa-patterns) |
| **[til](https://github.com/raghavatgit/til)** | Systems Notes | Markdown, Architecture | 110+ technical notes covering Linux VFS dentry cache, database storage engines, and memory management. | [Browse Notes ->](https://github.com/raghavatgit/til) |
| **[Zenflow-3D](https://github.com/raghavatgit/Zenflow-3D)** | Kinetic Motion | JavaScript, CSS3 Perspectives | Deep focus spatial interface implementing multi-layered perspective planes and tactile physics. | [View Prototype ->](https://github.com/raghavatgit/Zenflow-3D) |
| **[FoodStaticWebs](https://github.com/raghavatgit/FoodStaticWebs)** | Commercial Web | HTML5, CSS3 Grid, Responsive | Modern responsive culinary web design templates with fluid responsive layouts and fast load times. | [View Templates ->](https://github.com/raghavatgit/FoodStaticWebs) |

---

### Engineering Activity & Live Telemetry

<div align="center">
  <img src="assets/snake.svg?v=5" alt="Contribution Snake Animation" width="100%" />
</div>

<br />

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=raghavatgit&theme=tokyonight&hide_border=true&background=0A0D16&stroke=30363D&ring=58A6FF&fire=3FB950&currStreakLabel=58A6FF" alt="GitHub Streak" />
</div>

<br />

| Metric | Overview | Focus Area |
| :--- | :--- | :--- |
| **Annual Activity** | 720+ Contributions (Active Streak) | Algorithmic Problem Solving & Systems Development |
| **Problem Solutions** | 100+ Production-Grade Solutions | Rust, C++, TypeScript ([dsa-patterns](https://github.com/raghavatgit/dsa-patterns)) |
| **Systems & Architecture** | 110+ Technical Engineering Notes | Linux VFS, Distributed Systems, Networking ([til](https://github.com/raghavatgit/til)) |
| **Active Codebases** | 11 Public Repositories | Desktop Utilities, Web Audio DSP, Spatial 3D Web |

---

### Freelance Services & Client Solutions

- **Full-Stack Web Design & Prototyping**: Engineering bespoke, modern web applications, high-converting product landing pages, and interactive 3D spatial web experiences with zero bloated dependencies.
- **Native Desktop App Development**: Building high-efficiency desktop utilities and lightweight tools using Rust, Tauri, and TypeScript with minimal resource consumption.
- **End-to-End MVP Delivery**: Transforming product ideas into deployed, fully functional prototypes with automated CI/CD and edge cloud deployment on GCP and Firebase.

---

### Contact & Collaboration

Whether you are looking for a responsive full-stack web application, a custom native desktop utility, or an end-to-end prototype:

- **Portfolio**: [crag.web.app](https://crag.web.app)
- **Interactive Portal**: [contactraghav.web.app](https://contactraghav.web.app)
- **LinkedIn**: [linkedin.com/in/raghav-goyal-linkd](https://www.linkedin.com/in/raghav-goyal-linkd/)
- **Email**: [goyalraghav1289@gmail.com](mailto:goyalraghav1289@gmail.com)

<br />

<div align="center">
  <img src="assets/footer.svg?v=5" alt="Footer Banner" width="100%" />
</div>
