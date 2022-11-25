from unittest import mock
from toy_robot.toy_robot import ToyRobot


@mock.patch("toy_robot.toy_robot.input")
def test_run_1(mocked_input):
    commands = [
        "PLACE 0,0,NORTH",
        "MOVE",
        "REPORT",
    ]
    mocked_input.side_effect = commands
    tr = ToyRobot()
    result = tr.run()
    assert result == [0, 1, "NORTH"]


@mock.patch("toy_robot.toy_robot.input")
def test_run_2(mocked_input):
    commands = [
        "PLACE 0,0,NORTH",
        "LEFT",
        "REPORT",
    ]
    mocked_input.side_effect = commands
    tr = ToyRobot()
    result = tr.run()
    assert result == [0, 0, "WEST"]


@mock.patch("toy_robot.toy_robot.input")
def test_run_3(mocked_input):
    commands = [
        "PLACE 1,2,EAST",
        "MOVE",
        "MOVE",
        "LEFT",
        "MOVE",
        "REPORT"
    ]
    mocked_input.side_effect = commands
    tr = ToyRobot()
    result = tr.run()
    assert result == [3, 3, "NORTH"]


@mock.patch("toy_robot.toy_robot.input")
def test_run_4(mocked_input):
    commands = [
        "PLACE 5,5,NORTH",
        "MOVE",
        "MOVE",
        "MOVE",
        "REPORT"
    ]
    mocked_input.side_effect = commands
    tr = ToyRobot()
    result = tr.run()
    assert result == [5, 5, "NORTH"]


@mock.patch("toy_robot.toy_robot.input")
def test_run_5(mocked_input):
    commands = [
        "PLACE 5,5,WEST",
        "MOVE",
        "MOVE",
        "MOVE",
        "REPORT"
    ]
    mocked_input.side_effect = commands
    tr = ToyRobot()
    result = tr.run()
    assert result == [2, 5, "WEST"]


@mock.patch("toy_robot.toy_robot.input")
def test_run_6(mocked_input):
    commands = [
        "PLACE 3,3,SOUTH",
        "RIGHT",
        "REPORT"
    ]
    mocked_input.side_effect = commands
    tr = ToyRobot()
    result = tr.run()
    assert result == [3, 3, "EAST"]
