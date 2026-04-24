# 阶段一：构建
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# 阶段二：运行
FROM python:3.9-slim
WORKDIR /app

# 创建非 root 用户
RUN groupadd -r exporter && useradd -r -m -g exporter exporter

# 复制依赖和代码
COPY --from=builder --chown=exporter:exporter /root/.local /home/exporter/.local
COPY --chown=exporter:exporter exporter.py .

# 设置环境变量
ENV PATH=/home/exporter/.local/bin:$PATH
ENV PYTHONPATH=/home/exporter/.local/lib/python3.9/site-packages:$PYTHONPATH

# 切换用户
USER exporter
EXPOSE 8000

# 启动
CMD ["python", "exporter.py"]
