from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from logic import VotingSystem

class VoteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.voting_system = VotingSystem()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Voting System")
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Enter a candidate's name to vote:")
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        vote_button = QPushButton("Vote", self)
        vote_button.clicked.connect(self.cast_vote_by_name)
        layout.addWidget(vote_button)

        exit_button = QPushButton("Exit", self)
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        self.setLayout(layout)

    def cast_vote_by_name(self):
        candidate_name = self.input_field.text()
        if self.voting_system.is_valid_candidate(candidate_name):
            candidate_id = self.get_candidate_id_by_name(candidate_name)
            if candidate_id:
                self.voting_system.vote_for_candidate(candidate_id)
                self.update_display()
                QMessageBox.information(self, "Success", f"You've voted for {candidate_name}!")
        else:
            QMessageBox.warning(self, "Warning", "Please enter a valid candidate name.")

    def update_display(self):
        vote_count = self.voting_system.get_vote_count()
        total_votes = self.voting_system.get_total_votes()

        display_text = "\n".join([f"{self.voting_system.candidates[candidate]} - {count}" for candidate, count in vote_count.items()])
        display_text += f"\nTotal - {total_votes}"
        self.label.setText(display_text)

    def get_candidate_id_by_name(self, candidate_name):
        for candidate_id, name in self.voting_system.candidates.items():
            if name == candidate_name:
                return candidate_id
        return None

    def show_results(self):
        self.update_display()
