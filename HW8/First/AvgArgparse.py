import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", type=float, nargs="+", required=True,
                        help="The Student Grades List")

    parser.add_argument("-f", type=int, default=2, help="Sets Average Precision")

    args = parser.parse_args()
    print(f"Student Average= {float((sum(args.g) / len(args.g))):.{args.f}f}")

