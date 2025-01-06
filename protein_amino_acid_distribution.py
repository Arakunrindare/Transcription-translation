import matplotlib.pyplot as plt

# Amino acid categories
categories = {
    "Aromatic": ['F', 'W', 'Y'],
    "Acidic": ['D', 'E'],
    "Basic": ['K', 'R', 'H'],
    "Polar (Uncharged)": ['S', 'T', 'Q', 'N'],
    "Non-polar": ['A', 'V', 'I', 'L', 'M', 'P', 'G'],
    "Special Case (Sulfur)": ['C']
}

def calculate_aa_distribution(protein_sequence):
    """
    Calculate the percentage distribution of amino acids in the given protein sequence.
    :param protein_sequence: String of the protein sequence (amino acids)
    :return: Dictionary with percentages for each category
    """
    # Initialize counts
    total_aa = len(protein_sequence)
    distribution = {category: 0 for category in categories}

    # Count occurrences
    for aa in protein_sequence.upper():
        for category, residues in categories.items():
            if aa in residues:
                distribution[category] += 1
                break

    # Convert counts to percentages
    for category in distribution:
        distribution[category] = (distribution[category] / total_aa) * 100

    return distribution

def plot_pie_chart(distribution, filename):
    """
    Plot the amino acid distribution as a pie chart.
    :param distribution: Dictionary with percentages for each category
    :param filename: Name of the file to save the plot
    """
    labels = list(distribution.keys())
    sizes = list(distribution.values())

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Amino Acid Distribution in Protein Sequence")
    plt.savefig(filename)
    plt.show()
    print(f"Pie chart saved as {filename}.")

def plot_bar_chart(distribution, filename):
    """
    Plot the amino acid distribution as a nested bar plot.
    :param distribution: Dictionary with percentages for each category
    :param filename: Name of the file to save the plot
    """
    categories = list(distribution.keys())
    percentages = list(distribution.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, percentages, color='skyblue', edgecolor='black')
    plt.title("Amino Acid Distribution in Protein Sequence")
    plt.xlabel("Amino Acid Categories")
    plt.ylabel("Percentage")
    plt.ylim(0, 100)

    # Add percentage labels on top of bars
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f"{bar.get_height():.1f}%", ha='center', va='bottom')

    plt.savefig(filename)
    plt.show()
    print(f"Bar chart saved as {filename}.")

if __name__ == "__main__":
    print("Welcome to the Amino Acid Distribution Calculator!")
    protein_input = input("Enter a protein sequence: ").strip()
    
    # Calculate the distribution
    distribution = calculate_aa_distribution(protein_input)
    print("\nAmino Acid Distribution (in percentages):")
    for category, percentage in distribution.items():
        print(f"{category}: {percentage:.2f}%")

    # Ask the user for the plot type
    print("\nHow would you like to visualize the distribution?")
    print("1. Pie Chart")
    print("2. Bar Chart")
    choice = input("Enter 1 for Pie Chart or 2 for Bar Chart: ").strip()

    # File to save the plot
    filename = input("Enter a filename for the plot (e.g., plot.png): ").strip()

    # Plot and save
    if choice == '1':
        plot_pie_chart(distribution, filename)
    elif choice == '2':
        plot_bar_chart(distribution, filename)
    else:
        print("Invalid choice! Exiting.")
