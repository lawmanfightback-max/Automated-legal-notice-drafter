import datetime

def generate_legal_notice(advocate_name, client_name, recipient_name, cheque_no, cheque_date, amount, bank_name):
    notice_text = f"""
======================================================================
                         LEGAL DEMAND NOTICE
               (Under Section 138 of the Negotiable Instruments Act)
======================================================================

Date: {datetime.date.today().strftime('%d-%m-%Y')}

To,
{recipient_name}

Sir/Madam,

Under instructions and authority from my client, {client_name}, I hereby serve upon you the following statutory legal notice:

1. That you issued Cheque No. {cheque_no} dated {cheque_date} for an amount of INR {amount}/- drawn on {bank_name} in discharge of your legally enforceable liability towards my client.

2. That on presentation, the said cheque was dishonoured and returned unpaid by the bank with the remark "Funds Insufficient" vide Cheque Return Memo.

3. That you are hereby called upon to pay the outstanding amount of INR {amount}/- within 15 (fifteen) days from the receipt of this notice, failing which my client shall initiate criminal proceedings under Section 138 of the Negotiable Instruments Act against you, holding you liable for all legal costs and consequences.

Issued under instructions:

{advocate_name}
Advocate
"""
    return notice_text

if __name__ == "__main__":
    sample_notice = generate_legal_notice(
        advocate_name="Counsel / Advocate",
        client_name="ABC Business Corp",
        recipient_name="XYZ Traders Pvt Ltd",
        cheque_no="450123",
        cheque_date="10-09-2026",
        amount="2,50,000",
        bank_name="HDFC Bank"
    )
    print(sample_notice)
    
    # Save output to text file
    with open("Generated_Notice.txt", "w") as f:
        f.write(sample_notice)
    print("\n[SUCCESS] Notice generated and saved as 'Generated_Notice.txt'")
  
