def clean_titration_volumes(volumes):
    cleaned_volumes = [v for v in volumes if 5 <= v <= 50]
    return cleaned_volumes

# Sample calls
volumes1 = [3.2, 5.0, 12.5, 49.9, 51.0]
result1 = clean_titration_volumes(volumes1)
print(result1)

volumes2 = [4.9, 6.0, 25.0, 50.0, 50.1]
result2 = clean_titration_volumes(volumes2)
print(result2)

volumes3 = [5, 10, 20, 30, 40, 50]
result3 = clean_titration_volumes(volumes3)
print(result3)
