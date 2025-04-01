export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return 0;
  }
  return students.reduce((accumulator, currentValue) => accumulator + currentValue.id, 0);
}
