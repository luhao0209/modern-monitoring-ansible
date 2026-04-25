# 🚀 Modern Monitoring Stack (Ansible + GitHub Actions)

基于 Ansible 和 GitHub Actions 构建的自动化监控堆栈部署方案。
本项目致力于实现 **“零接触（Zero-Touch）”** 的一键式部署，专为国内复杂的网络环境进行了高可用（HA）网络容灾优化。

## 🌟 核心特性 (Key Features)

* **🖥️ 纯 Web UI 驱动部署：** 告别本地终端和繁琐的脚本！利用 GitHub Actions 的 `workflow_dispatch`，只需在网页表单输入新服务器的 IP 和密码，即可全自动触发云端部署流水线。
* **🛡️ 动态主机注入：** 流水线运行时动态生成 Ansible Inventory，彻底避免硬编码 IP 带来的维护成本（Toil）和安全风险。
* **🌐 镜像源高可用集群 (HA Registry Mirrors)：** 针对国内拉取 Docker Hub 镜像容易超时、被劫持或 0B 断流的痛点，内置了多节点公益镜像源代理池。Docker 引擎会自动进行故障转移和重试，保障部署的极致顺滑。
* **🔄 幂等性设计：** Ansible Playbook 确保了配置的幂等性，重复运行不会破坏现有环境，天然支持弹性扩展。

## 📦 包含的监控组件 (The Stack)



部署完成后，服务器将自动拉起以下云原生监控矩阵：
* **Prometheus:** 核心时序数据库，负责指标抓取与存储。
* **Grafana:** 强大的可视化大屏（内置 Node-Exporter 经典仪表盘）。
* **Alertmanager:** 告警路由与通知引擎。
* **Node-Exporter:** 宿主机硬件及操作系统指标采集器。

---

## 🛠️ 部署指南 (Deployment Guide)

### 1. 前置准备 (Prerequisites)
请确保你的目标云服务器（推荐 Ubuntu 系统）满足以下条件：
* 已开启并允许 root 用户通过密码登录。
* 如果是刚购买的阿里云/腾讯云服务器，请确保内部 SSH 配置允许密码验证：
  ```bash
  sed -i 's/^#*PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
  sed -i 's/^#*PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config
  systemctl restart sshd
