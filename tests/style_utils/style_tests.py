from feffery_dash_utils.style_utils import style


if __name__ == '__main__':
    print(
        style(
            fontSize=20,
            background='yellow',
        )
    )

    print(
        style(
            """
.IvkwhTOsc9wu6RdvHESR .yK52Sq0w7wspWaS28YNl {
    width: 91.46%;
    margin-left: 4.27%;
    margin-bottom: 5%;
    position: relative;
}"""
        )
    )

    print(
        style(
            """
.IvkwhTOsc9wu6RdvHESR .yK52Sq0w7wspWaS28YNl {
    width: 91.46%;
    margin-left: 4.27%;
    margin-bottom: 5%;
    position: relative;
}""",
            fontSize=18.8,
        )
    )
