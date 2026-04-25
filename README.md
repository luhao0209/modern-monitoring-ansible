# 现代云原生自动化监控部署栈

本项目致力于通过“基础设施即代码 (IaC)”理念，实现 Prometheus + Grafana + Alertmanager 监控体系在云服务器上的全自动化交付。

## ✨ 核心特性
* **一键自动化**：基于 Ansible Playbook，彻底消除手动配置服务器的繁琐步骤。
* **CI/CD 流水线**：集成 GitHub Actions，实现代码提交即触发多节点的免密并发部署。
* **环境隔离**：使用 Docker & Docker Compose 编排监控组件，保证开发与生产环境的绝对一致性。
* **安全交付**：采用非对称加密密钥托管，实现安全的零干预远程执行。

## 🚀 快速开始
1. 在 `inventory.ini` 中填入目标服务器的 IP 地址。
2. 将服务器对应的 SSH 私钥配置到 GitHub Secrets (`SERVER_SSH_KEY`) 中。
3. 提交代码至 `main` 分支，GitHub Actions 将自动接管并完成全部部署。
