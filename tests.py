height = 119
    output = run_io_fun("{}\n".format(height), rollercoaster)
    assert "Sorry, you're not tall enough to go on the ride." in output, f"Expected 'Sorry, you're not tall enough to go on the ride.', but got {output}"
