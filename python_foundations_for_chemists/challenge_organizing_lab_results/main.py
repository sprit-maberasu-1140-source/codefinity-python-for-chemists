def map_samples_to_pH(sample_names, pH_values, query_sample):
    
    sample_pH_dict = {}
    for i in range(len(sample_names)):
        sample_pH_dict[sample_names[i]]= pH_values[i]
    if query_sample in sample_pH_dict:
        result = sample_pH_dict[query_sample]
    else:
        result = None
    return sample_pH_dict,result

# Sample calls
sample_names = ["Sample A", "Sample B", "Sample C"]
pH_values = [7.2, 5.8, 8.1]
query_sample = "Sample B"
dictionary, pH = map_samples_to_pH(sample_names, pH_values, query_sample)
print(dictionary)
print(pH)

query_sample2 = "Sample X"
dictionary2, pH2 = map_samples_to_pH(sample_names, pH_values, query_sample2)
print(dictionary2)
print(pH2)
