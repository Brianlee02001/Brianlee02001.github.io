import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Doctor class represents a doctor with a name and specialization
class Doctor {
    private String name;
    private String specialization;

    public Doctor(String name, String specialization) {
        this.name = name;
        this.specialization = specialization;
    }

    public String getName() {
        return name;
    }

    public String getSpecialization() {
        return specialization;
    }
}

// Patient class represents a patient with a name, age, and assigned doctor
class Patient {
    private String name;
    private int age;
    private Doctor assignedDoctor;

    public Patient(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public Doctor getAssignedDoctor() {
        return assignedDoctor;
    }

    public void setAssignedDoctor(Doctor doctor) {
        this.assignedDoctor = doctor;
    }
}

// MedicalManagementSystem class manages doctors and patients
class MedicalManagementSystem {
    private List<Doctor> doctors;
    private List<Patient> patients;

    public MedicalManagementSystem() {
        doctors = new ArrayList<>();
        patients = new ArrayList<>();
    }

    public void addDoctor(Doctor doctor) {
        doctors.add(doctor);
    }

    public void addPatient(Patient patient) {
        patients.add(patient);
    }

    public void assignDoctorToPatient(Doctor doctor, Patient patient) {
        patient.setAssignedDoctor(doctor);
    }

    public void displayDoctors() {
        System.out.println("Doctors:");
        for (Doctor doctor : doctors) {
            System.out.println("Name: " + doctor.getName() + ", Specialization: " + doctor.getSpecialization());
        }
    }

    public void displayPatients() {
        System.out.println("Patients:");
        for (Patient patient : patients) {
            System.out.println("Name: " + patient.getName() + ", Age: " + patient.getAge() +
                    ", Assigned Doctor: " + (patient.getAssignedDoctor() != null ? patient.getAssignedDoctor().getName() : "None"));
        }
    }
}

// OnlineMedicalManagementSystem class is the main entry point of the program
public class OnlineMedicalManagementSystem {
    public static void main(String[] args) {
        MedicalManagementSystem system = new MedicalManagementSystem();

        // Create doctors
        Doctor doctor1 = new Doctor("Dr. Kim", "Pediatrician");
        Doctor doctor2 = new Doctor("Dr. Blue", "Dermatologist");

        // Add doctors to the system
        system.addDoctor(doctor1);
        system.addDoctor(doctor2);

        // Create patients
        Patient patient1 = new Patient("Michael", 11);
        Patient patient2 = new Patient("Brian", 12);

        // Add patients to the system
        system.addPatient(patient1);
        system.addPatient(patient2);

        // Assign doctors to patients
        system.assignDoctorToPatient(doctor1, patient1);
        system.assignDoctorToPatient(doctor2, patient2);

        Scanner scanner = new Scanner(System.in);
        int choice;
        do {
            System.out.println("=== Online Medical Management System ===");
            System.out.println("1. Display Doctors");
            System.out.println("2. Display Patients");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    // Display the list of doctors
                    system.displayDoctors();
                    break;
                case 2:
                    // Display the list of patients
                    system.displayPatients();
                    break;
                case 0:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
            System.out.println();
        } while (choice != 0);

        scanner.close();
    }
}
