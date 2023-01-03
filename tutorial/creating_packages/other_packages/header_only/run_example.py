from test.examples_tools import run


cmd_out = run("conan create .")
assert "1 + 3 = 4" in cmd_out

cmd_out = run("conan list sum/0.1#:*")
assert "Local Cache:" in cmd_out
assert ": da39a3ee5e6b4b0d3255bfef95601890afd80709" in cmd_out


cmd_out = run("conan create .")
assert "1 + 3 = 4" in cmd_out

cmd_out = run("conan list sum/0.1#:*")
assert "Local Cache:" in cmd_out
assert ": da39a3ee5e6b4b0d3255bfef95601890afd80709" in cmd_out

# FIXME: remove "No package info/revision was found" once beta8 is out
assert any([pkg_info in cmd_out for pkg_info in ["Empty package information", "No package info/revision was found"]])
