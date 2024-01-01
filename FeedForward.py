import torch.nn as nn
class ChordAI(nn.Module):
    def __init__(self, INPUT_SIZE, OUTPUT_SIZE):
        super().__init__()
        self.lstm = nn.LSTM(INPUT_SIZE, 64, batch_first=True)
        self.linear = nn.Linear(64, OUTPUT_SIZE)

    def forward(self, input_data):
        lstm_out, _ = self.lstm(input_data)
        predictions = self.linear(lstm_out)
        return predictions