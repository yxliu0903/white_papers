#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成示例JSON文件用于测试展示效果
"""

import json
import os
import random
from datetime import datetime, timedelta
import uuid

def generate_sample_json_files(num_files=50, output_dir="sample_json_files"):
    """
    生成示例JSON文件
    
    Args:
        num_files: 要生成的文件数量
        output_dir: 输出目录
    """
    
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 示例数据模板
    templates = [
        {
            "type": "user_data",
            "template": {
                "user_id": "",
                "username": "",
                "email": "",
                "profile": {
                    "age": 0,
                    "location": "",
                    "interests": []
                },
                "created_at": "",
                "last_login": "",
                "status": ""
            }
        },
        {
            "type": "config",
            "template": {
                "app_name": "",
                "version": "",
                "settings": {
                    "theme": "",
                    "language": "",
                    "notifications": True
                },
                "database": {
                    "host": "",
                    "port": 0,
                    "name": ""
                }
            }
        },
        {
            "type": "results",
            "template": {
                "experiment_id": "",
                "timestamp": "",
                "metrics": {
                    "accuracy": 0.0,
                    "precision": 0.0,
                    "recall": 0.0,
                    "f1_score": 0.0
                },
                "parameters": {},
                "status": ""
            }
        },
        {
            "type": "log",
            "template": {
                "log_id": "",
                "level": "",
                "message": "",
                "timestamp": "",
                "source": "",
                "details": {}
            }
        },
        {
            "type": "api_response",
            "template": {
                "request_id": "",
                "endpoint": "",
                "method": "",
                "status_code": 0,
                "response_time": 0.0,
                "data": {},
                "timestamp": ""
            }
        }
    ]
    
    # 示例数据
    usernames = ["alice", "bob", "charlie", "diana", "eve", "frank", "grace", "henry"]
    locations = ["北京", "上海", "广州", "深圳", "杭州", "成都", "西安", "武汉"]
    interests = ["编程", "音乐", "运动", "阅读", "旅行", "摄影", "烹饪", "游戏"]
    themes = ["light", "dark", "auto", "blue", "green"]
    languages = ["zh-CN", "en-US", "ja-JP", "ko-KR", "fr-FR"]
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]
    statuses = ["active", "inactive", "pending", "completed", "failed"]
    endpoints = ["/api/users", "/api/posts", "/api/comments", "/api/likes", "/api/search"]
    methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
    
    for i in range(num_files):
        # 随机选择模板
        template_info = random.choice(templates)
        template = template_info["template"].copy()
        
        # 根据模板类型填充数据
        if template_info["type"] == "user_data":
            template["user_id"] = str(uuid.uuid4())
            template["username"] = random.choice(usernames) + str(random.randint(1, 999))
            template["email"] = f"{template['username']}@example.com"
            template["profile"]["age"] = random.randint(18, 65)
            template["profile"]["location"] = random.choice(locations)
            template["profile"]["interests"] = random.sample(interests, random.randint(1, 4))
            template["created_at"] = (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat()
            template["last_login"] = (datetime.now() - timedelta(hours=random.randint(1, 168))).isoformat()
            template["status"] = random.choice(statuses)
            
        elif template_info["type"] == "config":
            template["app_name"] = f"App_{random.randint(1, 10)}"
            template["version"] = f"{random.randint(1, 5)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
            template["settings"]["theme"] = random.choice(themes)
            template["settings"]["language"] = random.choice(languages)
            template["settings"]["notifications"] = random.choice([True, False])
            template["database"]["host"] = f"db{random.randint(1, 5)}.example.com"
            template["database"]["port"] = random.choice([3306, 5432, 27017, 6379])
            template["database"]["name"] = f"database_{random.randint(1, 10)}"
            
        elif template_info["type"] == "results":
            template["experiment_id"] = f"exp_{random.randint(1000, 9999)}"
            template["timestamp"] = datetime.now().isoformat()
            template["metrics"]["accuracy"] = round(random.uniform(0.7, 0.99), 4)
            template["metrics"]["precision"] = round(random.uniform(0.6, 0.95), 4)
            template["metrics"]["recall"] = round(random.uniform(0.5, 0.9), 4)
            template["metrics"]["f1_score"] = round(random.uniform(0.6, 0.92), 4)
            template["parameters"] = {
                "learning_rate": round(random.uniform(0.001, 0.1), 6),
                "batch_size": random.choice([16, 32, 64, 128]),
                "epochs": random.randint(10, 100),
                "model_type": random.choice(["CNN", "RNN", "Transformer", "MLP"])
            }
            template["status"] = random.choice(statuses)
            
        elif template_info["type"] == "log":
            template["log_id"] = str(uuid.uuid4())
            template["level"] = random.choice(log_levels)
            template["message"] = f"这是一条{template['level']}级别的日志消息"
            template["timestamp"] = datetime.now().isoformat()
            template["source"] = f"module_{random.randint(1, 10)}"
            template["details"] = {
                "user_id": random.randint(1, 1000),
                "action": random.choice(["login", "logout", "create", "update", "delete"]),
                "ip_address": f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
            }
            
        elif template_info["type"] == "api_response":
            template["request_id"] = str(uuid.uuid4())
            template["endpoint"] = random.choice(endpoints)
            template["method"] = random.choice(methods)
            template["status_code"] = random.choice([200, 201, 400, 401, 404, 500])
            template["response_time"] = round(random.uniform(0.1, 2.0), 3)
            template["data"] = {
                "items": random.randint(1, 50),
                "total": random.randint(50, 1000),
                "page": random.randint(1, 10)
            }
            template["timestamp"] = datetime.now().isoformat()
        
        # 生成文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{template_info['type']}_{timestamp}_{i+1:03d}.json"
        filepath = os.path.join(output_dir, filename)
        
        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(template, f, ensure_ascii=False, indent=2)
        
        print(f"已生成: {filename}")
    
    print(f"\n成功生成 {num_files} 个JSON文件到目录: {output_dir}")

def generate_large_json_file(output_dir="sample_json_files", filename="large_dataset.json"):
    """
    生成一个大的JSON文件，包含多个数据项
    """
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 生成大量数据
    data = []
    for i in range(1000):
        item = {
            "id": i + 1,
            "name": f"Item_{i+1}",
            "category": random.choice(["A", "B", "C", "D", "E"]),
            "value": round(random.uniform(0, 1000), 2),
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat(),
            "metadata": {
                "tags": random.sample(["tag1", "tag2", "tag3", "tag4", "tag5"], random.randint(1, 3)),
                "priority": random.randint(1, 5),
                "status": random.choice(["active", "inactive", "pending"])
            },
            "nested_data": {
                "level1": {
                    "level2": {
                        "level3": {
                            "value": random.randint(1, 100),
                            "description": f"这是第{i+1}个项目的详细描述"
                        }
                    }
                }
            }
        }
        data.append(item)
    
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"已生成大型JSON文件: {filename}")

if __name__ == "__main__":
    print("开始生成示例JSON文件...")
    
    # 生成50个不同类型的JSON文件
    generate_sample_json_files(50)
    
    # 生成一个大的JSON文件
    generate_large_json_file()
    
    print("\n所有文件生成完成！")
    print("现在您可以打开 json_files_display.html 来查看效果")
    print("或者使用以下命令启动一个简单的HTTP服务器:")
    print("python -m http.server 8000")
    print("然后在浏览器中访问: http://localhost:8000/json_files_display.html") 