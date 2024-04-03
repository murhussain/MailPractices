import random

# Given spam and ham word lists
spam_list = ['buy', 'discount', 'click', 'free', 'offer', 'winner', 'prize', 'cash', 'urgent', 'money',
             'limited', 'special', 'deal', 'offer', 'sale', 'bonus', 'credit', 'card', 'gift', 'guarantee',
             'now', 'only', 'today', 'order', 'shop', 'shipping']

ham_list = ['meeting', 'tomorrow', 'lunch', 'dinner', 'coffee', 'work', 'project', 'team', 'meeting',
            'office', 'time', 'date', 'place', 'schedule', 'appointment', 'discussion', 'call', 'email',
            'message', 'phone', 'contact', 'address', 'number', 'home', 'office', 'work', 'week', 'month']


# Functions to create emails
def create_email(word_list):
    return ' '.join(random.choices(word_list, k=5))


def create_emails(num_emails=5, is_spam=True):
    emails = []
    word_list = spam_list if is_spam else ham_list
    for _ in range(num_emails):
        emails.append(create_email(word_list))
    return emails


# Count occurrences of each word in a list of emails
def count_words(emails):
    word_counts = {}
    for email in emails:
        for word in email.split():
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


# Calculate P(w|category) for each word in a category
def calculate_word_probabilities(word_counts, total_words):
    return {word: (count / total_words) for word, count in word_counts.items()}


# Compute the likelihood ratio for each word
def compute_likelihood_ratios(spam_probs, ham_probs):
    return {word: (spam_probs.get(word, 0) / ham_probs.get(word, 0.0001)) for word in set(spam_probs) | set(ham_probs)}


# Main script
if __name__ == '__main__':
    num_emails = 10
    spam_emails = create_emails(num_emails, is_spam=True)
    ham_emails = create_emails(num_emails, is_spam=False)

    # Count words in each category
    spam_counts = count_words(spam_emails)
    ham_counts = count_words(ham_emails)
    total_spam_words = sum(spam_counts.values())
    total_ham_words = sum(ham_counts.values())

    # Calculate word probabilities in each category
    spam_probs = calculate_word_probabilities(spam_counts, total_spam_words)
    ham_probs = calculate_word_probabilities(ham_counts, total_ham_words)

    # Compute likelihood ratios
    likelihood_ratios = compute_likelihood_ratios(spam_probs, ham_probs)

    # Print the likelihood ratios
    for word, ratio in likelihood_ratios.items():
        print(
            f"Word: '{word}', P(w|Spam): {spam_probs.get(word, 0)}, P(w|Ham): {ham_probs.get(word, 0)}, Likelihood Ratio: {ratio}")