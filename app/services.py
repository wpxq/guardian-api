import docker, psutil

client = docker.from_env()

def get_docker_status():
    containers = client.containers.list(all=True)
    return [
        {
            "id": c.short_id,
            "name": c.name,
            "status": c.status,
            "image": str(c.image.tags[0] if c.image.tags else "unknown")
        } for c in containers
    ]

def get_system_stats():
    return {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "ram_usage": psutil.virtual_memory().percent
    }
    
def get_detailed_stats():
    containers = client.containers.list()
    stats_list = []
    for c in containers:
        s = c.stats(stream=False)
        mem_usage = s['memory_stats']['usage']
        stats_list.append({
            "name": c.name,
            "mem_usage_wb": round(mem_usage, 2),
            "cpu_details": s['cpu_stats']['cpu_usage']['total_usage']
        })
    return stats_list