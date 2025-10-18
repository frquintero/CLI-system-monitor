# System metrics collection module

import psutil
from typing import Dict, Any


def get_cpu_usage() -> float:
    """Get current CPU usage percentage."""
    try:
        return psutil.cpu_percent(interval=1)
    except Exception:
        return 0.0


def get_memory_info() -> Dict[str, Any]:
    """Get memory usage information."""
    try:
        mem = psutil.virtual_memory()
        return {
            'used': mem.used,
            'total': mem.total,
            'percentage': mem.percent
        }
    except Exception:
        return {'used': 0, 'total': 0, 'percentage': 0.0}


def get_disk_info() -> Dict[str, Any]:
    """Get disk usage information for root partition."""
    try:
        disk = psutil.disk_usage('/')
        return {
            'used': disk.used,
            'total': disk.total,
            'percentage': disk.percent
        }
    except Exception:
        return {'used': 0, 'total': 0, 'percentage': 0.0}


def get_network_info() -> Dict[str, Any]:
    """Get network activity information."""
    try:
        net = psutil.net_io_counters()
        if net is None:
            return {'bytes_sent': 0, 'bytes_recv': 0, 'packets_sent': 0, 'packets_recv': 0}
        return {
            'bytes_sent': net.bytes_sent,
            'bytes_recv': net.bytes_recv,
            'packets_sent': net.packets_sent,
            'packets_recv': net.packets_recv
        }
    except Exception:
        return {'bytes_sent': 0, 'bytes_recv': 0, 'packets_sent': 0, 'packets_recv': 0}


def get_all_metrics() -> Dict[str, Any]:
    """Get all system metrics."""
    return {
        'cpu': get_cpu_usage(),
        'memory': get_memory_info(),
        'disk': get_disk_info(),
        'network': get_network_info()
    }