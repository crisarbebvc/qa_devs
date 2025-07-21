import json, glob

def unify_results():
    data = []
    for file in glob.glob('results/test_results_*.json'):
        with open(file) as f:
            data.append(json.load(f))
    with open('results/unified_summary.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    unify_results()
