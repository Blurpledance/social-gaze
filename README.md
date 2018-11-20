
# Methods

## Materials

Stimuli are computer generated floating head models (video type = .avi).

- 192 unique stimuli
- 8 unique identities

Identity race is a 50/50 split between black and white.

- White = 1, 2, 3, 4
- Black = 5, 6, 7, 8

Identity sex is a 50/50 split between male and female.

- Females = f
- Males = m

8 variations per identity. Each variation a combination of 6 dichotomous features (Eye Contact, direction, speed)

- Gaze = Eye contact or No eye contact (labeled EC or NC)
- Direction =  The direction the stimuli turn from (labeled Left or Right)
- Speed =  How speed at which the stimuli turn to center (fast = 2) (slow = 3)

Example label for a stimuli using identity m_1 that is fast, makes eye contact, and turns from the right : m_1_EC_right_3

## Trials

Faces are divided into two blocks (majority eye contact, and majority no eye contact)

- Each block contains 48 stimuli (a total of 96 are viewed)
- 67% of the stimuli in the majority eye contact block make eye contact (EC).
- 67% of the stimuli in the majority no eye contact block do not make eye contact (NC).

Additionally, these blocks are randomly assigned to be either active or passive.
- Passive blocks require participants to passively view the stimuli.
- Active blocks ask participants to indicate with the arrow keys, which direction the stimuli turned from.

Digital input numbers are assigned to each stimuli so that acqKnowledge is able to acurately track on the onset and offset of each stimuli to the participant's physio acitivty.

Either a 0 or 1 is assigned to each of the previously desicribe stimuli features (sex, race, eye contact, direction, speed), as well as which block they are in (passive or active)

- Sex: 0=male 1=female
- Race: 0=white, 1=black
- Direction: 0=right, 1=left
- Speed: 0=2, 1=3
- Eye contact: 0=EC, 1=NC
- Block majority: 0=NC, 1=EC
- Block type: 0=Passive, 1=Active

m1_EC_right_3 in an active majority eye contact block would have a DIN of 0001011

## Procedure

1. Participant arrives.
1. EKG and EDA sensors are applied to the participant.
1. Physio data is collected via BioPac, and recorded on the program AcqKnowledge.
1. Open the command prompt.
1. Call python.
1. Run the file titled "Experiment_PC_Final"
1. Enter the participant number into the resulting window.
1. Baseline data is collected for five minutes. Instructions are displayed.
1. At the start of the baseline period a digital input number is used to denote in the AcqKnowledge file when the exact start and stop time for the baseline period is.
1. Upon completion of the baseline period, instructions for the task are displayed.
1. Participants begin task.
1. Before stimuli presentation, an fixation cross, acompanied by an orienting sound, appears for 250 ms.
1. Stimuli are presented for 7 seconds at a time (4 seconds of video, 3 seconds of paused image). The appropriate DIN acompanies each stimuli and is recorded in the AcqKnowledge program.
1. Inter-stimulus duration equals 8s (8.25 if not including fixation cross).
1. After the presentation of all 48 stimuli in the first block, there is a 2 minute waiting period before the second block.
1. The second block is presented (if the first was passive, the second is active. IF the first was majority EC, the second is majority NC).
