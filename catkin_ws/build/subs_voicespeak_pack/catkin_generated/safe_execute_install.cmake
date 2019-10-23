execute_process(COMMAND "/home/kyungman/catkin_ws/build/subs_voicespeak_pack/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/kyungman/catkin_ws/build/subs_voicespeak_pack/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
