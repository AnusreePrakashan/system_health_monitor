import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
import os

# Import the functions from the script
from system_health_monitor import check_cpu_usage, check_memory_usage, check_disk_usage, check_running_processes

class TestSystemHealthMonitor(unittest.TestCase):

    @patch('psutil.cpu_percent')
    def test_check_cpu_usage_high(self, mock_cpu_percent):
        mock_cpu_percent.return_value = 85.0  # Mock a high CPU usage
        with patch('sys.stdout', new=StringIO()) as fake_out:
            check_cpu_usage()
            self.assertIn('High CPU usage detected', fake_out.getvalue())

    @patch('psutil.virtual_memory')
    def test_check_memory_usage_high(self, mock_virtual_memory):
        mock_virtual_memory.return_value.percent = 85.0  # Mock a high memory usage
        with patch('sys.stdout', new=StringIO()) as fake_out:
            check_memory_usage()
            self.assertIn('High Memory usage detected', fake_out.getvalue())

    @patch('psutil.disk_usage')
    def test_check_disk_usage_high(self, mock_disk_usage):
        mock_disk_usage.return_value.percent = 85.0  # Mock a high disk usage
        with patch('sys.stdout', new=StringIO()) as fake_out:
            check_disk_usage()
            self.assertIn('High Disk usage detected', fake_out.getvalue())

    @patch('psutil.pids')
    def test_check_running_processes_high(self, mock_pids):
        mock_pids.return_value = list(range(250))  # Mock a high number of running processes
        with patch('sys.stdout', new=StringIO()) as fake_out:
            check_running_processes()
            self.assertIn('High number of running processes detected', fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
