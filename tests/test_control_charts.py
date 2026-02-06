import control_charts as dt
import pyshewhart
import matplotlib.pyplot as plt
import pandas as pd


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = dt.add_offset(augend, addend)
    assert expected == obtained


measurements = pd.read_csv("tests/data/Lambda_W.csv")


def test_example():
    pyshewhart.XbarR(measurements["fecha"], measurements["Lambda"],
                     sample_size=4)
    plt.savefig("control_chart_lambda.png")
    plt.close()

    pyshewhart.XbarR(measurements["fecha"], measurements["W"],
                     sample_size=4, check_western_elec_rules=False)
    plt.savefig("control_chart_w.png")
    plt.close()
