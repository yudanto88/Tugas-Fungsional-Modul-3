def konversi():
    def minggu(minggu_value):
        def hari(hari_value):
            def jam(jam_value):
                def menit(menit_value):
                    total_menit = (
                        (minggu_value * 7 * 24 * 60)
                        + (hari_value * 24 * 60)
                        + (jam_value * 60)
                        + menit_value
                    )
                    return total_menit

                return menit

            return jam

        return hari

    return minggu

data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]

for item in data:
    values = item.split()
    minggu_value = int(values[0])
    hari_value = int(values[2])
    jam_value = int(values[4])
    menit_value = int(values[6])

    konvert = konversi()(minggu_value)(hari_value)(jam_value)(menit_value)

    print(f"{item}, konversi: {konvert} menit")

result = []

for item in data:
    parts = item.split()

    minggu = 0
    hari = 0
    jam = 0
    menit = 0

    if "minggu" in item:
        minggu = int(parts[0])
    if "hari" in item:
        hari = int(parts[parts.index("hari") - 1])
    if "jam" in item:
        jam = int(parts[parts.index("jam") - 1])
    if "menit" in item:
        menit = int(parts[parts.index("menit") - 1])

    formatted_time = f"{minggu}:{hari}:{jam}:{menit}"

    result.append(formatted_time)

print(result)
