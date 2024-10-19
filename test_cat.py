from click.testing import CliRunner
from pycat.pycat import main

def test_read_single_file(tmpdir):
    test_file = tmpdir.join("test_file.txt")
    test_file.write("Hello, World!")

    runner = CliRunner()

    result = runner.invoke(main, [str(test_file)])

    assert result.exit_code == 0
    assert result.output == "Hello, World!\n"


def test_read_multiple_files(tmpdir):
    test_file1 = tmpdir.join("file1.txt")
    test_file1.write("Content of First File")

    test_file2 = tmpdir.join("file2.txt")
    test_file2.write("Contents of Second File")

    runner = CliRunner()

    result = runner.invoke(main, [str(test_file1), str(test_file2)])

    assert result.exit_code == 0
    assert result.output == "Content of First File\nContents of Second File\n"

def test_non_existent_file():
    runner = CliRunner()

    result = runner.invoke(main, ["nonexistentfile.txt"])

    assert result.exit_code != 0
    assert "Error" in result.output

def test_empty_file(tmpdir):
    empty_file = tmpdir.join('empty.txt')
    empty_file.write("")

    runner = CliRunner()

    result = runner.invoke(main, [str(empty_file)])

    assert result.exit_code == 0
    assert result.output == "\n"

def test_concatenate_file(tmpdir):
    file1 = tmpdir.join("test_file1.txt")
    file1.write("Content of First File")

    file2 = tmpdir.join("test_file2.txt")
    file2.write("Content of Second File")

    runner = CliRunner()

    result = runner.invoke(main, [str(file1), str(file2)])

    assert result.exit_code == 0
    assert result.output == "Content of First File\nContent of Second File\n"

