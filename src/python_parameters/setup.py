from setuptools import find_packages, setup

package_name = 'python_parameters'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi',
    maintainer_email='pi@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          #  'minimal_param_node = python_parameters.python_parameters_node:main',
            'listener = python_parameters.subscriber_member_function:main',
            'talker= python_parameters.publisher_member_function:main',
            'imu_listener= python_parameters.subscriber_imu_function:main',
        ],
    },
)
