# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "/usr/local/include;/vol/rcp/tiago-nightly/include;/vol/rcp/tiago-nightly/include/gazebo-8;/vol/rcp/tiago-nightly/include/bullet;/vol/rcp/tiago-nightly/include/simbody;/usr/include;/vol/rcp/tiago-nightly/include/sdformat-5.3;/vol/rcp/tiago-nightly/include/ignition/math3;/usr/include/OGRE;/usr/include/OGRE/Terrain;/usr/include/OGRE/Paging;/vol/rcp/tiago-nightly/include/ignition/transport3;/usr/include/uuid;/vol/rcp/tiago-nightly/include/ignition/msgs0".split(';') if "/usr/local/include;/vol/rcp/tiago-nightly/include;/vol/rcp/tiago-nightly/include/gazebo-8;/vol/rcp/tiago-nightly/include/bullet;/vol/rcp/tiago-nightly/include/simbody;/usr/include;/vol/rcp/tiago-nightly/include/sdformat-5.3;/vol/rcp/tiago-nightly/include/ignition/math3;/usr/include/OGRE;/usr/include/OGRE/Terrain;/usr/include/OGRE/Paging;/vol/rcp/tiago-nightly/include/ignition/transport3;/usr/include/uuid;/vol/rcp/tiago-nightly/include/ignition/msgs0" != "" else []
PROJECT_CATKIN_DEPENDS = "std_msgs;std_srvs;tf;pal_multirobot_msgs;roscpp;control_toolbox".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lgazebo_ros_forcetorque;-lgazebo_pal_hand;-lgazebo_wifi_ap;-lgazebo_underactuated_finger;-lBulletSoftBody;-lBulletDynamics;-lBulletCollision;-lLinearMath;/vol/rcp/tiago-nightly/lib/libSimTKsimbody.so;/vol/rcp/tiago-nightly/lib/libSimTKmath.so;/vol/rcp/tiago-nightly/lib/libSimTKcommon.so;/usr/lib/liblapack.so;/usr/lib/libf77blas.so;/usr/lib/libatlas.so;-lpthread;-lrt;-ldl;-lm;/vol/rcp/tiago-nightly/lib/libgazebo.so;/vol/rcp/tiago-nightly/lib/libgazebo_client.so;/vol/rcp/tiago-nightly/lib/libgazebo_gui.so;/vol/rcp/tiago-nightly/lib/libgazebo_sensors.so;/vol/rcp/tiago-nightly/lib/libgazebo_rendering.so;/vol/rcp/tiago-nightly/lib/libgazebo_physics.so;/vol/rcp/tiago-nightly/lib/libgazebo_ode.so;/vol/rcp/tiago-nightly/lib/libgazebo_transport.so;/vol/rcp/tiago-nightly/lib/libgazebo_msgs.so;/vol/rcp/tiago-nightly/lib/libgazebo_util.so;/vol/rcp/tiago-nightly/lib/libgazebo_common.so;/vol/rcp/tiago-nightly/lib/libgazebo_gimpact.so;/vol/rcp/tiago-nightly/lib/libgazebo_opcode.so;/vol/rcp/tiago-nightly/lib/libgazebo_opende_ou.so;/vol/rcp/tiago-nightly/lib/libgazebo_math.so;/usr/lib/x86_64-linux-gnu/libboost_signals.so;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;/usr/lib/x86_64-linux-gnu/libboost_program_options.so;/usr/lib/x86_64-linux-gnu/libboost_regex.so;/usr/lib/x86_64-linux-gnu/libboost_iostreams.so;/vol/rcp/tiago-nightly/lib/libsdformat.so;/usr/lib/x86_64-linux-gnu/libOgreMain.so;/usr/lib/x86_64-linux-gnu/libOgreTerrain.so;/usr/lib/x86_64-linux-gnu/libOgrePaging.so;/vol/rcp/tiago-nightly/lib/libignition-transport3.so;/vol/rcp/tiago-nightly/lib/libprotobuf.so;-lzmq;-luuid;/vol/rcp/tiago-nightly/lib/libignition-msgs0.so.0.7.0;/vol/rcp/tiago-nightly/lib/libignition-math3.so.3.3.0;/usr/lib/x86_64-linux-gnu/libboost_thread.so;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;/usr/lib/x86_64-linux-gnu/libboost_system.so;/usr/lib/x86_64-linux-gnu/libboost_date_time.so;/usr/lib/x86_64-linux-gnu/libboost_atomic.so;/usr/lib/x86_64-linux-gnu/libpthread.so".split(';') if "-lgazebo_ros_forcetorque;-lgazebo_pal_hand;-lgazebo_wifi_ap;-lgazebo_underactuated_finger;-lBulletSoftBody;-lBulletDynamics;-lBulletCollision;-lLinearMath;/vol/rcp/tiago-nightly/lib/libSimTKsimbody.so;/vol/rcp/tiago-nightly/lib/libSimTKmath.so;/vol/rcp/tiago-nightly/lib/libSimTKcommon.so;/usr/lib/liblapack.so;/usr/lib/libf77blas.so;/usr/lib/libatlas.so;-lpthread;-lrt;-ldl;-lm;/vol/rcp/tiago-nightly/lib/libgazebo.so;/vol/rcp/tiago-nightly/lib/libgazebo_client.so;/vol/rcp/tiago-nightly/lib/libgazebo_gui.so;/vol/rcp/tiago-nightly/lib/libgazebo_sensors.so;/vol/rcp/tiago-nightly/lib/libgazebo_rendering.so;/vol/rcp/tiago-nightly/lib/libgazebo_physics.so;/vol/rcp/tiago-nightly/lib/libgazebo_ode.so;/vol/rcp/tiago-nightly/lib/libgazebo_transport.so;/vol/rcp/tiago-nightly/lib/libgazebo_msgs.so;/vol/rcp/tiago-nightly/lib/libgazebo_util.so;/vol/rcp/tiago-nightly/lib/libgazebo_common.so;/vol/rcp/tiago-nightly/lib/libgazebo_gimpact.so;/vol/rcp/tiago-nightly/lib/libgazebo_opcode.so;/vol/rcp/tiago-nightly/lib/libgazebo_opende_ou.so;/vol/rcp/tiago-nightly/lib/libgazebo_math.so;/usr/lib/x86_64-linux-gnu/libboost_signals.so;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;/usr/lib/x86_64-linux-gnu/libboost_program_options.so;/usr/lib/x86_64-linux-gnu/libboost_regex.so;/usr/lib/x86_64-linux-gnu/libboost_iostreams.so;/vol/rcp/tiago-nightly/lib/libsdformat.so;/usr/lib/x86_64-linux-gnu/libOgreMain.so;/usr/lib/x86_64-linux-gnu/libOgreTerrain.so;/usr/lib/x86_64-linux-gnu/libOgrePaging.so;/vol/rcp/tiago-nightly/lib/libignition-transport3.so;/vol/rcp/tiago-nightly/lib/libprotobuf.so;-lzmq;-luuid;/vol/rcp/tiago-nightly/lib/libignition-msgs0.so.0.7.0;/vol/rcp/tiago-nightly/lib/libignition-math3.so.3.3.0;/usr/lib/x86_64-linux-gnu/libboost_thread.so;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;/usr/lib/x86_64-linux-gnu/libboost_system.so;/usr/lib/x86_64-linux-gnu/libboost_date_time.so;/usr/lib/x86_64-linux-gnu/libboost_atomic.so;/usr/lib/x86_64-linux-gnu/libpthread.so" != "" else []
PROJECT_NAME = "pal_gazebo_plugins"
PROJECT_SPACE_DIR = "/usr/local"
PROJECT_VERSION = "1.1.4"
