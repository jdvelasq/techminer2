"""
Abstracts Summarization (NO --- requiere pytorch)
===============================================================================


# >>> directory = "data/regtech/"

# >>> from techminer2 import tm2__abstractive_summarization
# >>> tm2__abstractive_summarization(
# ...     criterion="author_keywords",
# ...     custom_topics=["blockchain"],
# ...     n_abstracts=20,    
# ...     directory=directory,
# ... )


"""
# import os
# import textwrap

# # from transformers import GPT2LMHeadModel, GPT2Tokenizer

# from ._read_records import read_records


# def tm2__abstractive_summarization(
#     criterion,
#     custom_topics,
#     file_name="abstractive_summarization.txt",
#     n_abstracts=50,
#     directory="./",
#     database="documents",
#     start_year=None,
#     end_year=None,
#     **filters,
# ):
#     """Abstract extractive summarization using sumy."""

#     records = read_records(
#         directory=directory,
#         database=database,
#         start_year=start_year,
#         end_year=end_year,
#         **filters,
#     )

#     records = _select_records(criterion, custom_topics, n_abstracts, records)
#     document = _create_document(records)

#     tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
#     model = GPT2LMHeadModel.from_pretrained("gpt2")

#     inputs = tokenizer.batch_encode_plus(
#         [document], return_tensors="pt", max_length=512
#     )
#     summary_ids = model.generate(inputs["input_ids"], early_stopping=True)

#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#     with open(
#         os.path.join(directory, "reports", file_name), "w", encoding="utf-8"
#     ) as out_file:

#         print(summary, file=out_file)

#     print(summary)


# def _create_document(records):
#     abstracts = records["abstract"]
#     abstracts = abstracts.dropna()
#     document = "\n".join(abstracts.tolist())
#     return document


# def _select_records(criterion, custom_topics, n_abstracts, records):
#     selected_records = records[["article", criterion]]
#     selected_records[criterion] = selected_records[criterion].str.split(";")
#     selected_records = selected_records.explode(criterion)
#     selected_records[criterion] = selected_records[criterion].str.strip()
#     selected_records = selected_records[selected_records[criterion].isin(custom_topics)]
#     records = records[records["article"].isin(selected_records["article"])]

#     records = records.sort_values(
#         by=["global_citations", "local_citations"], ascending=False
#     )
#     records = records.head(n_abstracts)
#     return records
