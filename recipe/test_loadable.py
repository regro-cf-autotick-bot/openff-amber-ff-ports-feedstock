from openff.toolkit import ForceField

for improper in [True, False]:
    for version in range(1, 5):
        ForceField(f"ff14sb_{'off_impropers_' if improper else ''}0.0.{version}.offxml")
