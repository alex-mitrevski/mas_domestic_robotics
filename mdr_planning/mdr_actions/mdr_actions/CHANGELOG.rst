^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package mdr_actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.2.0 (2017-11-04)
------------------

1.1.2 (2017-10-29)
------------------

1.1.1 (2017-09-20)
------------------
* Change maintainer tags to MAS Robotics
* Update changelog for mdr_planning
* Contributors: Argentina Ortega Sainz

1.1.0 (2017-09-18 18:15)
------------------------

1.0.1 (2017-09-18 18:04)
------------------------
* Merge branch 'refactor/mdr_planning' into 'indigo'
  Move actions, behaviors, and scenarios to a new mdr_planning metapackage
  See merge request !25
* Refactored mdr_actions (made mdr_actions a metapackage and created separate packages for the existing actions)
* Contributors: Alex Mitrevski

1.0.0 (2017-04-11 10:44:12 +0200)
---------------------------------
* Merge branch 'perceive_table' into 'indigo'
  Merge Perceive Table Skill to indigo
  See merge request !17
* Fix run_tests problem
* Fix roslint issue
* Merge branch 'indigo' into 'perceive_table'
  # Conflicts:
  #   mdr_behaviors/mdr_actions/CMakeLists.txt
  #   mdr_behaviors/mdr_actions/ros/src/mdr_actions/action_states.py
* Add perceive_table skill from minh/go2017 branch
* Merge branch 'inspection-test' into 'indigo'
  [scenarios] actions and SM for robot inspection test
  See merge request !15
* [scenarios] actions and SM for robot inspection test
* Contributors: Minh Nguyen, Santosh Thoduka
