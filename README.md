# Quick App

Quick App is a real-time chat application built using Django, providing users with features like user authentication, friend suggestions, emoji integration, and profile management.

## Features

- **User Authentication:** Users can register, login, and authenticate to access the chat application securely.

- **Friend Suggestions:** Quick App suggests friends based on user interests and connections, allowing users to send friend requests and connect with others easily.

- **Emoji Integration:** Emoji selector integrated into the chat interface, enabling users to express themselves with a wide range of emojis.

- **Profile Management:** Users can update their profiles, including editing their name, profile photo, username, and other details to personalize their experience.

## Superuser Credentials

To access the admin panel and perform administrative tasks, you can use the following superuser credentials:

- **Username:** admin
- **Password:** admin

## Getting Started

Follow these steps to get started with Quick App:

1. Clone the repository:

```
git clone https://github.com/ravi300601/Quickchat.git
```

3. Install dependencies:
```
pip install -r requirements.txt
```

3. Apply database migrations:
```
python manage.py migrate
```

4. Create a superuser:
```
python manage.py createsuperuser
```

5. Run the development server:
```
python manage.py runserver
```

6. Access the application at `http://127.0.0.1:8000/` and start chatting!

## Contributing

Contributions are welcome! If you'd like to contribute to Quick App, please follow these guidelines:

- Fork the repository.
- Create a new branch (`git checkout -b feature/improvement`)
- Commit your changes (`git commit -am 'Add new feature'`)
- Push to the branch (`git push origin feature/improvement`)
- Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.

## Acknowledgements
Quick App is built using the Django framework and various open-source libraries. We would like to extend our gratitude to the developers of these tools for their contributions.
