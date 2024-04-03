import random
import math

# Given spam and ham word lists
spam_list = ['buy', 'discount', 'click', 'free', 'offer', 'winner', 'prize', 'cash', 'urgent', 'money',
             'limited', 'special', 'deal', 'offer', 'sale', 'bonus', 'credit', 'card', 'gift', 'guarantee',
             'now', 'only', 'today', 'order', 'shop', 'shipping']

ham_list = ['meeting', 'tomorrow', 'lunch', 'dinner', 'coffee', 'work', 'project', 'team', 'meeting',
            'office', 'time', 'date', 'place', 'schedule', 'appointment', 'discussion', 'call', 'email',
            'message', 'phone', 'contact', 'address', 'number', 'home', 'office', 'work', 'week', 'month']


def create_email(word_list):
    return ' '.join(random.choices(word_list, k=5))


def create_emails(num_emails=5, is_spam=True):
    emails = []
    word_list = spam_list if is_spam else ham_list
    for _ in range(num_emails):
        emails.append(create_email(word_list))
    return emails


def count_words(emails):
    word_counts = {}
    for email in emails:
        for word in email.split():
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def calculate_word_probabilities(word_counts, total_words):
    return {word: (count / total_words) for word, count in word_counts.items()}


def create_random_email(spam_list, ham_list, length=5):
    mixed_list = spam_list + ham_list
    return ' '.join(random.choices(mixed_list, k=length))


def classify_email(email, spam_probs, ham_probs):
    words = email.split()
    spam_log_likelihood = 0
    ham_log_likelihood = 0

    for word in words:
        spam_log_likelihood += math.log(spam_probs.get(word, 1e-5))  # Using a small probability for unseen words
        ham_log_likelihood += math.log(ham_probs.get(word, 1e-5))

    return "Spam" if spam_log_likelihood > ham_log_likelihood else "Ham"


# Main script
if __name__ == '__main__':
    num_emails = 100  # Adjust the number of generated emails for training
    spam_emails = create_emails(num_emails, is_spam=True)
    ham_emails = create_emails(num_emails, is_spam=False)

    spam_counts = count_words(spam_emails)
    ham_counts = count_words(ham_emails)
    total_spam_words = sum(spam_counts.values())
    total_ham_words = sum(ham_counts.values())

    spam_probs = calculate_word_probabilities(spam_counts, total_spam_words)
    ham_probs = calculate_word_probabilities(ham_counts, total_ham_words)

    # Create a new random email
    new_email = create_random_email(spam_list, ham_list)

    # Classify the new email
    classification = classify_email(new_email, spam_probs, ham_probs)

    print(f"New Email: {new_email}")
    print(f"Classified as: {classification}")

    # Print probabilities
    print("\nSpam Probabilities:")
    for word, prob in spam_probs.items():
        print(f"Word: '{word}', P(w|Spam): {prob}")

    print("\nHam Probabilities:")
    for word, prob in ham_probs.items():
        print(f"Word: '{word}', P(w|Ham): {prob}")
