from cmp_expert.data.pipeline import build_corpus

if __name__ == '__main__':
    build_corpus('./data/raw', './data/processed/sft.jsonl')
