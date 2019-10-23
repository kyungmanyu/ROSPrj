#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/kyungman/catkin_ws/src/subs_ros_pack"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/kyungman/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/kyungman/catkin_ws/install/lib/python2.7/dist-packages:/home/kyungman/catkin_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/kyungman/catkin_ws/build" \
    "/usr/bin/python2" \
    "/home/kyungman/catkin_ws/src/subs_ros_pack/setup.py" \
    build --build-base "/home/kyungman/catkin_ws/build/subs_ros_pack" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/kyungman/catkin_ws/install" --install-scripts="/home/kyungman/catkin_ws/install/bin"
